from fastapi import FastAPI

app = FastAPI(title="EvalForge")

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}