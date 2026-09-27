from fastapi import FastAPI

from app.evaluation_case import EvaluationCase
from app.evaluation_result import EvaluationResult, calculate_precision_recall

app = FastAPI(title="EvalForge")

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}

@app.post("/eval-runs")
async def run_evaluation(evaluation_case: EvaluationCase) -> EvaluationResult:
    result = calculate_precision_recall(evaluation_case.expected_rules, evaluation_case.actual_rules)
    return result