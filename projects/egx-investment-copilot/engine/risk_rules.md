# Risk Rules — V1

## Portfolio
- Starting capital: EGP 5,000
- Default maximum risk per tactical trade: 1.5% of equity
- Hard maximum risk per trade: 2% of equity
- No leverage or margin
- No automatic execution

## Position sizing

`max_loss_egp = equity * risk_percent`

`risk_per_share = abs(entry - stop_loss)`

`shares = floor(max_loss_egp / risk_per_share)`

Then cap by available cash and any liquidity/portfolio concentration rule.

## Signal gate
A BUY signal is blocked when:
- market data is stale or unverified
- stop loss is missing
- risk/reward is below the configured minimum
- liquidity is insufficient for the intended position
- portfolio concentration would exceed configured limits

## Default target
Use staged exits where appropriate. The engine must preserve the exact entry, stop and target assumptions used when the signal was generated.
