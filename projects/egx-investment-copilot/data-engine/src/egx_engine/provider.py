from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from typing import Any

import httpx

from .models import DailyBar, MarketSnapshot


class MarketDataError(RuntimeError):
    pass


class MarketDataProvider(ABC):
    name: str

    @abstractmethod
    def snapshot(self, ticker: str) -> MarketSnapshot:
        raise NotImplementedError

    @abstractmethod
    def daily_bars(self, ticker: str, start: date, end: date) -> list[DailyBar]:
        raise NotImplementedError


class EGXAPIProvider(MarketDataProvider):
    """Thin market-data adapter; intentionally has no order-routing methods."""

    name = "egxapi"

    def __init__(self, api_key: str, base_url: str = "https://api.egxapi.com", timeout: float = 10.0):
        if not api_key:
            raise ValueError("MARKET_DATA_API_KEY is required")
        self.client = httpx.Client(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
        )

    def _get(self, path: str, params: dict[str, Any]) -> Any:
        try:
            response = self.client.get(path, params=params)
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise MarketDataError(f"{self.name} request failed: {exc}") from exc

    @staticmethod
    def _rows(payload: Any) -> list[dict[str, Any]]:
        if isinstance(payload, list):
            return [x for x in payload if isinstance(x, dict)]
        if isinstance(payload, dict):
            for key in ("data", "bars", "results", "items", "quotes"):
                value = payload.get(key)
                if isinstance(value, list):
                    return [x for x in value if isinstance(x, dict)]
            if all(isinstance(v, (str, int, float, type(None))) for v in payload.values()):
                return [payload]
        raise MarketDataError("Unexpected market-data payload shape")

    def daily_bars(self, ticker: str, start: date, end: date) -> list[DailyBar]:
        payload = self._get(
            "/v2/market-data/bars",
            {"symbol": ticker, "from": start.isoformat(), "to": end.isoformat()},
        )
        bars: list[DailyBar] = []
        for row in self._rows(payload):
            session_date = row.get("date") or row.get("session_date") or row.get("timestamp")
            bars.append(
                DailyBar(
                    ticker=ticker,
                    session_date=session_date,
                    open=Decimal(str(row["open"])),
                    high=Decimal(str(row["high"])),
                    low=Decimal(str(row["low"])),
                    close=Decimal(str(row["close"])),
                    volume=int(row.get("volume", 0)),
                    source=self.name,
                )
            )
        return bars

    def snapshot(self, ticker: str) -> MarketSnapshot:
        """Return the latest available bar, explicitly marked stale if old.

        This is intentionally temporary: a dedicated real-time quote contract
        must replace this method before live trading decisions are enabled.
        """
        today = datetime.now(timezone.utc).date()
        bars = self.daily_bars(ticker, today - timedelta(days=7), today)
        if not bars:
            raise MarketDataError(f"No market data returned for {ticker}")

        bar = max(bars, key=lambda item: item.session_date)
        source_timestamp = datetime.combine(bar.session_date, datetime.min.time(), tzinfo=timezone.utc)
        freshness = max(0, int((datetime.now(timezone.utc) - source_timestamp).total_seconds()))
        return MarketSnapshot(
            instrument_id=ticker,
            ticker=ticker,
            timestamp_utc=source_timestamp,
            session_date=bar.session_date,
            last_price=bar.close,
            open=bar.open,
            high=bar.high,
            low=bar.low,
            volume=bar.volume,
            source=self.name,
            source_timestamp=source_timestamp,
            freshness_seconds=freshness,
        )
