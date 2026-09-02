from fastapi import FastAPI

app = FastAPI(title="EGX Investment Copilot Engine", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "egx-market-engine", "version": "0.1.0"}
