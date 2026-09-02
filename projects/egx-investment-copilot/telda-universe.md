# Telda-First Investment Universe

## V1 rule
Only instruments that are actually available for purchase through the user's Telda Invest account may receive a BUY/SELL recommendation.

EGX-listed alone is not sufficient.

## Verification status
Telda Securities is licensed for securities brokerage by Egypt's FRA (license 715). FRA also approved Telda Securities to receive subscriptions in investment fund certificates in 2025.

Public sources do not provide a complete, continuously updated list of instruments available inside every Telda account. Therefore the system must not assume that every EGX-listed security is tradable on Telda.

## MVP approach
Maintain a small manually verified universe from the instruments visible in the user's Telda Invest app. Store:
- ticker
- company/fund name
- asset type
- sector
- Telda available = true/false
- last verified date

Only `Telda available = true` instruments enter the AI ranking pipeline.

## Data priority
1. Telda-visible universe (execution compatibility)
2. EGX / licensed market data (market facts)
3. Company filings / official disclosures (fundamentals and catalysts)
4. Reputable financial news (context)

## Safety rule
If Telda availability or market data cannot be verified: `DATA NOT VERIFIED — NO TRADE`.

## V1 exclusions
- automatic order execution
- securities not verified as available on Telda
- leverage/margin
- derivatives
- unsupported funds/instruments
