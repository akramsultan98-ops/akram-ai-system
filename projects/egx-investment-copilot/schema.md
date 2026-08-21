# Normalized Market Data Schema — V1

All timestamps are stored in UTC plus an explicit `market_timezone=Africa/Cairo` field.

## instruments
- instrument_id
- ticker
- isin
- name
- exchange
- sector
- asset_type
- currency
- status
- source
- source_updated_at

## market_snapshots
- snapshot_id
- instrument_id
- timestamp_utc
- market_timezone
- session_date
- market_phase
- last_price
- bid
- ask
- open
- high
- low
- previous_close
- volume
- traded_value_egp
- bid_depth
- ask_depth
- source
- source_timestamp
- freshness_seconds
- validation_status

## daily_bars
- instrument_id
- session_date
- open
- high
- low
- close
- adjusted_close
- volume
- traded_value_egp
- corporate_action_adjusted
- source

## fundamentals
- instrument_id
- period_end
- fiscal_period
- revenue
- net_income
- eps
- book_value_per_share
- total_assets
- total_debt
- cash
- operating_cash_flow
- free_cash_flow
- roe
- roa
- pe
- pb
- dividend_yield
- source
- published_at

## news_events
- event_id
- published_at
- source
- headline
- url
- instrument_id (nullable)
- sector (nullable)
- event_type
- materiality
- sentiment
- summary
- raw_reference

## signals
- signal_id
- created_at
- instrument_id
- action
- entry_low
- entry_high
- stop_loss
- target_1
- target_2
- target_3
- position_egp
- shares
- risk_egp
- reward_egp
- risk_reward
- confidence
- market_regime
- thesis
- invalidation
- data_snapshot_id
- model
- status

## portfolio_positions
- position_id
- instrument_id
- shares
- average_entry
- current_price
- invested_egp
- market_value_egp
- realized_pnl_egp
- unrealized_pnl_egp
- stop_loss
- target_1
- target_2
- target_3
- thesis
- opened_at
- updated_at
- status

## portfolio
- portfolio_id
- base_currency
- initial_capital_egp
- cash_egp
- invested_egp
- market_value_egp
- total_equity_egp
- realized_pnl_egp
- unrealized_pnl_egp
- drawdown_pct
- risk_budget_pct
- updated_at

## executions
- execution_id
- instrument_id
- side
- shares
- execution_price
- execution_time
- fees_egp
- source (user_reported|broker_statement)
- telegram_message_id

## principle
The database stores facts and decisions. Claude never becomes the source of truth for prices, balances, fills, or calculations.
