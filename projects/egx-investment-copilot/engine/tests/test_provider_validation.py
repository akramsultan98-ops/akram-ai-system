import pytest

from providers.oanor import ProviderError, validate_quote


def test_valid_quote_is_normalized():
    result = validate_quote(
        "COMI",
        {"price": 100, "change": 1.25, "volume": 50000},
    )
    assert result["symbol"] == "COMI"
    assert result["price"] == 100.0
    assert result["provider"] == "oanor"


def test_missing_fields_are_rejected():
    with pytest.raises(ProviderError, match="DATA NOT VERIFIED"):
        validate_quote("COMI", {"price": 100, "change": 1.25})


def test_invalid_price_is_rejected():
    with pytest.raises(ProviderError, match="DATA NOT VERIFIED"):
        validate_quote("COMI", {"price": 0, "change": 1.25, "volume": 10})
