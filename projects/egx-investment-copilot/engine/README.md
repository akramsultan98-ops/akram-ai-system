# EGX Investment Copilot — Market Engine

Phase 2 establishes a deterministic analytics layer between market data and AI decision-making.

## Responsibilities
- Normalize market data
- Validate freshness and completeness
- Calculate technical indicators deterministically
- Calculate position sizing and risk/reward
- Produce a structured analysis packet for Claude
- Never issue an executable order

## Pipeline

Market Adapter → Validation → Indicators → Risk Engine → Analysis Packet → Claude

## Hard rules
1. Missing/stale market data must block a trade signal.
2. Prices, indicators, position sizing and risk calculations are computed by code, not hallucinated by an LLM.
3. Claude receives structured facts and is responsible for interpretation and decision quality.
4. V1 is recommendation-only; execution remains manual in Telda.
5. Every signal must be reproducible from stored input data.
