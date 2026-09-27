from pydantic import BaseModel

class EvaluationResult(BaseModel):
    true_positives: list[str]
    false_positives: list[str]
    false_negatives: list[str]
    precision: float
    recall: float
    
def calculate_precision_recall(expected_rules: list[str], actual_rules: list[str]) -> EvaluationResult:
    # Duplicate rule ids are ignored by converting to sets
    expected = set(expected_rules)
    actual = set(actual_rules)
    
    if not expected and not actual:
        return EvaluationResult(
            true_positives=[],
            false_positives=[],
            false_negatives=[],
            precision=1.0,
            recall=1.0
        )

    true_positives = sorted(expected & actual)
    false_positives = sorted(actual - expected)
    false_negatives = sorted(expected - actual)

    precision_denominator = len(true_positives) + len(false_positives)

    precision = (
        len(true_positives) / precision_denominator
        if precision_denominator > 0
        else 0.0
    )
    
    recall_denominator = len(true_positives) + len(false_negatives)
    recall = (
        len(true_positives) / recall_denominator
        if recall_denominator > 0
        else 0.0
    )
    
    return EvaluationResult(
        true_positives=true_positives,
        false_positives=false_positives,
        false_negatives=false_negatives,
        precision=precision,
        recall=recall
    )