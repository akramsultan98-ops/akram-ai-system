# V1 Build Order

## 1. Data adapter
Implement one provider adapter behind a stable interface:
- health()
- instruments()
- snapshot(symbols)
- daily_bars(symbol, start, end)

## 2. Validation
Reject stale/contradictory records before analytics.

## 3. Analytics
Compute deterministic indicators and risk metrics in Python.
Claude receives validated facts only.

## 4. Candidate ranking
Filter the full EGX universe to a small candidate set using liquidity, trend, momentum, and risk/reward gates.

## 5. Claude decision layer
Use a strong reasoning model only on the shortlisted candidates.

## 6. Portfolio memory
Persist signals, user-reported executions, positions, and cash in PostgreSQL.

## 7. Telegram
Send only actionable alerts and important position-state changes.

## 8. n8n
Orchestrate schedules, provider calls, retries, Telegram delivery, and user commands. Do not put core financial calculations inside n8n expressions.

## 9. Hetzner
Deploy after local validation. Keep PostgreSQL private, secrets outside Git, and expose only the required webhook/reverse-proxy surface.

## 10. Backtest gate
No real-money recommendation until the strategy has a reproducible historical backtest and the data pipeline passes freshness/quality checks.
