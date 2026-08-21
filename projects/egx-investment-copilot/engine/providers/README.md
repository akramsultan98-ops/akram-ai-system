# EGX Market Data Providers

## Current adapter: OANOR

OANOR currently advertises an EGX API with quote, screener, and EGX30 index endpoints. It is implemented here as an **opt-in adapter**, not as an approved production trading source.

Before production use:

1. Obtain provider credentials.
2. Confirm the commercial/data licensing terms.
3. Confirm whether the feed is real-time, delayed, or end-of-day for our subscription.
4. Run live integration tests against EGX reference values.
5. Compare timestamps and selected quotes against an independent source.
6. Only then enable the provider for signal generation.

If credentials are absent or validation fails, the engine must return:

`DATA NOT VERIFIED — NO TRADE`
