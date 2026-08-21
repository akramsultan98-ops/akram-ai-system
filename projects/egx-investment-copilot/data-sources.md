# EGX Market Data Layer

## Source hierarchy

### 1. Exchange / licensed source
Use EGX or a properly licensed institutional feed as the authoritative reference where available.

### 2. EGX.news
Current research indicates EGX.news offers EGX-specific live quotes, bid/ask, volume, market depth, 1-minute OHLCV, and historical daily data, with API/file delivery available by access request. Access and licensing terms must be confirmed before production use.

### 3. Secondary verification source
Use an independent source for cross-checking prices and corporate events. It must never silently overwrite the primary source.

### 4. News/fundamentals
Keep news, financial statements, earnings, corporate actions, and price data as separate datasets. Every item needs a timestamp and source identifier.

## Current candidate assessment

| Source | Live | Historical | Depth | API | Production decision |
|---|---|---|---|---|---|
| EGX / licensed feed | Depends on licensed access | Yes | Depends | Yes via licensed products | Target authoritative source |
| EGX.news | Advertises live | Yes | Advertises Level 2 | Access by request | Strong prototype candidate; verify terms |
| ICE EGX feed | Yes | Yes | Yes | Yes | Institutional fallback; likely overkill for EGP 5k |
| EGXAPI | Advertises live + trading API | Yes | Advertises order book | Yes | Do not use for live decisions until independently verified |

## Validation requirements

A market snapshot is valid only when:

- timestamp is current and timezone is explicit (Africa/Cairo)
- ticker is recognized
- price is numeric and positive
- bid/ask relationship is valid when present
- OHLC relationships are valid
- volume is non-negative
- source is known
- data age is below the configured freshness threshold
- duplicate/conflicting records are resolved deterministically

If validation fails: `DATA_NOT_VERIFIED_NO_TRADE`.

## Trading session assumptions

Do not hard-code trading hours into the decision engine. Load the exchange calendar/session configuration and store it with each snapshot. Current EGX.news documentation advertises live coverage during 09:00–15:30 Cairo time; this must be treated as a source claim and verified against the official exchange calendar before production scheduling.

## Important

Do not scrape a public web page as the primary production feed when a licensed/API source is available. Do not infer real-time prices from search snippets. Do not let an LLM fill missing numerical fields.
