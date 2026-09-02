from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any


@dataclass(frozen=True)
class Quote:
    ticker: str
    observed_at: datetime
    price: Decimal | None
    previous_close: Decimal | None
    volume: Decimal | None
    bid: Decimal | None
    ask: Decimal | None
    source: str
    quality_status: str


class MarketDataProvider:
    """Provider interface. Implement a licensed EGX source here; never put credentials in code."""

    name = "UNCONFIGURED"

    def quote(self, ticker: str) -> Quote:
        raise NotImplementedError


class UnconfiguredProvider(MarketDataProvider):
    def quote(self, ticker: str) -> Quote:
        raise RuntimeError("No validated EGX market-data provider configured")


def validate_quote(quote: Quote) -> None:
    if quote.quality_status != "VERIFIED":
        raise ValueError("DATA NOT VERIFIED — NO TRADE")
    if quote.price is None or quote.price <= 0:
        raise ValueError("Invalid quote price")
    if quote.bid is not None and quote.ask is not None and quote.bid > quote.ask:
        raise ValueError("Invalid bid/ask relationship")
