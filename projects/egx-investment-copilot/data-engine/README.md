# EGX Data Engine V1

Deterministic Python layer between market-data providers and Claude.

## Contract

`Provider → Normalize → Validate → Risk/Analytics → Claude`

Claude never receives raw provider payloads. It receives normalized, validated facts with provenance.

## Local setup

```bash
cd projects/egx-investment-copilot/data-engine
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest -q
```

## Provider

V1 contains an EGXAPI adapter for market-data bars. EGXAPI currently documents REST/WebSocket market data and exposes a `/v2/market-data/bars` endpoint in its public product documentation. Provider response shapes must be contract-tested before production use.

No order-routing code belongs in this package.

## Safety

- stale/invalid data must not reach the decision layer
- position sizing is deterministic
- maximum initial risk is 1.5% of equity
- minimum R/R is 1:2
- execution remains manual in Telda
