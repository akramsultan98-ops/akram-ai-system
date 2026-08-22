from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
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
    """Thin adapter around EGXAPI market-data endpoints.

    The adapter deliberately does not expose order-routing methods. V1 is
    data + decision support only; execution remains manual in Telda.
    """

    name = "egxapi"

    def __init__(self, api_key: str, base_url: str = "https://api.egxapi.com", timeout: float = 10.0):
        if not api_key:
            raise ValueError("MARKET_DATA_API_KEY is required")
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(
            base_url=self.base_url,
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
        payload = self._get("/v2/market-data/bars", {"symbol": ticker, "from": start.isoformat(), "to": end.isoformat()})
        rows = self._rows(payload)
        bars: list[DailyBar] = []
        for row in rows:
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
        # V1 uses the latest returned bar as a normalized snapshot until the
        # provider's dedicated quote endpoint is wired and contract-tested.
        today = date.today()
        bars = self.daily_bars(ticker, today, today)
        if not bars:
            raise MarketDataError(f"No market data returned for {ticker}")
        bar = bars[-1]
        now = bar.session_date
        from datetime import datetime, timezone
        timestamp = datetime(now.year, now.month, now.day, tzinfo=timezone.utc)
        return MarketSnapshot(
            instrument_id=ticker,
            ticker=ticker,
            timestamp_utc=timestamp,
            session_date=bar.session_date,
            last_price=bar.close,
            open=bar.open,
            high=bar.high,
            low=bar.low,
            volume=bar.volume,
            source=self.name,
            source_timestamp=timestamp,
            freshness_seconds=0,
        )
