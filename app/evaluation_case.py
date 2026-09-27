from pydantic import BaseModel

class EvaluationCase(BaseModel):
    id: str
    expected_rules: list[str]
    actual_rules: list[str]