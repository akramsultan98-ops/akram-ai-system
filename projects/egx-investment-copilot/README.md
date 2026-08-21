# EGX Investment Copilot

Personal AI portfolio-management assistant for an initial EGP 5,000 portfolio.

## Mission
Provide evidence-grounded, risk-controlled investment decisions for Egyptian Exchange (EGX) securities and track the portfolio step by step through Telegram.

## V1 execution model
- Human-in-the-loop only.
- No automatic trade execution.
- User executes approved trades manually in Telda.
- User reports fills to Telegram; the system records them and manages the position afterward.

## Architecture
Market Data → n8n → Python Analytics/Risk Engine → Claude Sonnet Scanner → Claude Opus Decision Layer → PostgreSQL Portfolio Memory → Telegram → User → Telda

## Phase 1 status
- [x] GitHub project initialized
- [x] Phase 1 issue created
- [x] Candidate market-data sources researched
- [ ] Finalize licensed market-data access
- [ ] Implement data adapters
- [ ] Implement normalized schema
- [ ] Implement validation/freshness gates
- [ ] Deploy to Hetzner
- [ ] Build n8n workflows
- [ ] Connect Telegram

## Data safety rule
If current market data cannot be verified, the system must output `DATA_NOT_VERIFIED_NO_TRADE` and must not generate a buy/sell signal.

## Risk rule
The system optimizes risk-adjusted expected value, not maximum speculative return. Every tactical position requires an entry, invalidation/stop, target(s), position size, and expected risk/reward.
