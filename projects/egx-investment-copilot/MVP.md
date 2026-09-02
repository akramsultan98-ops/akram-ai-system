# EGX Investment Copilot — Simple MVP

## Goal
Give Akram a simple, accurate, actionable Telegram message for managing an initial EGP 5,000 EGX portfolio through Telda.

## V1 stack
- Market data + financial/news sources
- n8n for scheduling and orchestration
- Claude Opus for analysis and final decision
- PostgreSQL only for portfolio/trade memory
- Telegram for alerts and confirmations
- Telda for manual execution
- Hetzner + Docker for hosting

## Explicitly out of scope for V1
- Automatic trade execution
- Level-2/order-book infrastructure
- Machine learning
- Multiple AI agents
- Kubernetes/microservices
- Complex backtesting platform
- Dozens of market-data providers
- Leverage, margin, derivatives, short selling

## Decision flow
1. Collect current market prices, volume, index state, financial information, news and corporate announcements.
2. Validate freshness and source reliability.
3. Give the verified data to Claude Opus.
4. Claude evaluates market regime, candidates, valuation, technical setup, catalysts and risk/reward.
5. Claude produces one of: BUY, BUY ON DIP, HOLD, SELL, WAIT / NO TRADE.
6. n8n sends one concise Telegram message.
7. Akram executes manually in Telda.
8. Akram replies with the fill; n8n updates the portfolio.
9. The system follows the open position until exit or invalidation.

## Accuracy rule
Never fabricate a current price, volume, ratio, news item, or market condition. If current data cannot be verified: DATA NOT VERIFIED — NO TRADE.

## Capital rule
Starting capital: EGP 5,000.
No need to deploy all capital. Cash is allowed when risk/reward is poor.

## Telegram commands
/start — initialize or show portfolio
/status — current portfolio and P/L
/scan — request a fresh market scan
/portfolio — show open positions and cash
/skip — skip the latest proposed trade

After manual execution, the user can send:
BOUGHT TICKER PRICE SHARES
SOLD TICKER PRICE SHARES

## Core output
Every actionable alert must contain:
- Ticker/name
- Current verified price
- Action
- Entry zone
- Allocation in EGP
- Stop loss
- Target 1 and Target 2
- Risk/reward
- 2–3 reasons
- Invalidation condition
- Data timestamp

## Operating principle
The system optimizes for risk-adjusted decision quality, not maximum activity. No trade is a valid outcome.
