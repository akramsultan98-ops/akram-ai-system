"""OANOR EGX provider adapter.

This adapter is intentionally opt-in. A provider response is never treated as
tradeable until freshness, required fields, and provider status are validated.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any

import httpx


BASE_URL = os.getenv("EGX_OANOR_BASE_URL", "https://api.oanor.com/egx-api")


class ProviderError(RuntimeError):
    pass


async def get_quote(symbol: str) -> dict[str, Any]:
    key = os.getenv("EGX_OANOR_API_KEY")
    if not key:
        raise ProviderError("DATA NOT VERIFIED — NO TRADE: EGX_OANOR_API_KEY is not configured")

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{BASE_URL}/v1/quote",
            params={"symbol": symbol},
            headers={"x-oanor-key": key},
        )

    if response.status_code != 200:
        raise ProviderError(f"Provider HTTP {response.status_code}")

    payload = response.json()
    if not isinstance(payload, dict):
        raise ProviderError("Invalid provider payload")

    return validate_quote(symbol, payload)


def validate_quote(symbol: str, payload: dict[str, Any]) -> dict[str, Any]:
    required = ("price", "change", "volume")
    missing = [field for field in required if payload.get(field) is None]
    if missing:
        raise ProviderError(f"DATA NOT VERIFIED — NO TRADE: missing {', '.join(missing)}")

    price = float(payload["price"])
    if price <= 0:
        raise ProviderError("DATA NOT VERIFIED — NO TRADE: invalid price")

    return {
        "symbol": symbol.upper(),
        "price": price,
        "change": float(payload["change"]),
        "volume": float(payload["volume"]),
        "provider": "oanor",
        "validated_at": datetime.now(timezone.utc).isoformat(),
    }
