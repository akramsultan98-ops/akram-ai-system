CREATE TABLE IF NOT EXISTS instruments (
  id BIGSERIAL PRIMARY KEY,
  ticker TEXT NOT NULL UNIQUE,
  name TEXT,
  sector TEXT,
  currency CHAR(3) NOT NULL DEFAULT 'EGP',
  exchange TEXT NOT NULL DEFAULT 'EGX',
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS market_snapshots (
  id BIGSERIAL PRIMARY KEY,
  instrument_id BIGINT NOT NULL REFERENCES instruments(id),
  observed_at TIMESTAMPTZ NOT NULL,
  source TEXT NOT NULL,
  price NUMERIC(18,6),
  open NUMERIC(18,6),
  high NUMERIC(18,6),
  low NUMERIC(18,6),
  previous_close NUMERIC(18,6),
  volume NUMERIC(24,6),
  bid NUMERIC(18,6),
  ask NUMERIC(18,6),
  change_pct NUMERIC(12,6),
  data_delay_seconds INTEGER,
  quality_status TEXT NOT NULL DEFAULT 'UNVERIFIED',
  raw_payload JSONB,
  UNIQUE(instrument_id, observed_at, source)
);

CREATE TABLE IF NOT EXISTS daily_bars (
  instrument_id BIGINT NOT NULL REFERENCES instruments(id),
  trading_date DATE NOT NULL,
  open NUMERIC(18,6) NOT NULL,
  high NUMERIC(18,6) NOT NULL,
  low NUMERIC(18,6) NOT NULL,
  close NUMERIC(18,6) NOT NULL,
  volume NUMERIC(24,6),
  source TEXT NOT NULL,
  PRIMARY KEY (instrument_id, trading_date, source)
);

CREATE TABLE IF NOT EXISTS fundamentals (
  id BIGSERIAL PRIMARY KEY,
  instrument_id BIGINT NOT NULL REFERENCES instruments(id),
  period_end DATE,
  source TEXT NOT NULL,
  revenue NUMERIC(24,6),
  net_income NUMERIC(24,6),
  eps NUMERIC(18,6),
  pe NUMERIC(18,6),
  pb NUMERIC(18,6),
  roe NUMERIC(18,6),
  debt NUMERIC(24,6),
  operating_cash_flow NUMERIC(24,6),
  dividend_yield NUMERIC(18,6),
  raw_payload JSONB,
  observed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS news_events (
  id BIGSERIAL PRIMARY KEY,
  instrument_id BIGINT REFERENCES instruments(id),
  published_at TIMESTAMPTZ,
  source TEXT NOT NULL,
  title TEXT NOT NULL,
  url TEXT,
  event_type TEXT,
  sentiment NUMERIC(8,4),
  raw_payload JSONB,
  UNIQUE(source, url)
);

CREATE TABLE IF NOT EXISTS portfolios (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  base_currency CHAR(3) NOT NULL DEFAULT 'EGP',
  starting_cash NUMERIC(18,2) NOT NULL,
  cash NUMERIC(18,2) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS positions (
  id BIGSERIAL PRIMARY KEY,
  portfolio_id BIGINT NOT NULL REFERENCES portfolios(id),
  instrument_id BIGINT NOT NULL REFERENCES instruments(id),
  quantity NUMERIC(24,6) NOT NULL DEFAULT 0,
  average_entry NUMERIC(18,6),
  stop_loss NUMERIC(18,6),
  target_1 NUMERIC(18,6),
  target_2 NUMERIC(18,6),
  target_3 NUMERIC(18,6),
  thesis TEXT,
  status TEXT NOT NULL DEFAULT 'OPEN',
  opened_at TIMESTAMPTZ,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(portfolio_id, instrument_id)
);

CREATE TABLE IF NOT EXISTS executions (
  id BIGSERIAL PRIMARY KEY,
  portfolio_id BIGINT NOT NULL REFERENCES portfolios(id),
  instrument_id BIGINT NOT NULL REFERENCES instruments(id),
  side TEXT NOT NULL CHECK (side IN ('BUY','SELL')),
  quantity NUMERIC(24,6) NOT NULL,
  price NUMERIC(18,6) NOT NULL,
  fees NUMERIC(18,6) NOT NULL DEFAULT 0,
  executed_at TIMESTAMPTZ NOT NULL,
  broker TEXT NOT NULL DEFAULT 'TELDA',
  external_reference TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS signals (
  id BIGSERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  instrument_id BIGINT REFERENCES instruments(id),
  action TEXT NOT NULL CHECK (action IN ('BUY','BUY_ON_DIP','HOLD','WATCH','REDUCE','SELL','NO_TRADE')),
  confidence NUMERIC(5,2),
  entry_low NUMERIC(18,6),
  entry_high NUMERIC(18,6),
  stop_loss NUMERIC(18,6),
  target_1 NUMERIC(18,6),
  target_2 NUMERIC(18,6),
  target_3 NUMERIC(18,6),
  risk_reward NUMERIC(10,4),
  position_size_egp NUMERIC(18,2),
  market_regime TEXT,
  rationale JSONB,
  invalidation TEXT,
  data_timestamp TIMESTAMPTZ,
  data_quality TEXT NOT NULL DEFAULT 'UNVERIFIED',
  status TEXT NOT NULL DEFAULT 'PENDING'
);

CREATE INDEX IF NOT EXISTS idx_market_snapshots_instrument_time ON market_snapshots(instrument_id, observed_at DESC);
CREATE INDEX IF NOT EXISTS idx_daily_bars_instrument_date ON daily_bars(instrument_id, trading_date DESC);
CREATE INDEX IF NOT EXISTS idx_news_events_published ON news_events(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_signals_created ON signals(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_executions_portfolio_time ON executions(portfolio_id, executed_at DESC);
