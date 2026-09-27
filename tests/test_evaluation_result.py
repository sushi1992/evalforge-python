from app.evaluation_case import EvaluationCase
from app.evaluation_result import calculate_precision_recall

def test_evaluation_case():
    case = EvaluationCase(
        id="test_case_1",
        expected_rules=["rule1", "rule2"],
        actual_rules=["rule1", "rule3"]
    )

    assert case.id == "test_case_1"
    assert case.expected_rules == ["rule1", "rule2"]
    assert case.actual_rules == ["rule1", "rule3"]
    
def test_evaluation_case_empty_lists():
    case = EvaluationCase(
        id="test_case_2",
        expected_rules=[],
        actual_rules=[]
    )

    assert case.id == "test_case_2"
    assert case.expected_rules == []
    assert case.actual_rules == []
    
def test_evaluation_case_with_duplicates():
    case = EvaluationCase(
        id="test_case_3",
        expected_rules=["rule1", "rule1", "rule2"],
        actual_rules=["rule1", "rule3", "rule3"]
    )

    assert case.id == "test_case_3"
    assert case.expected_rules == ["rule1", "rule1", "rule2"]
    assert case.actual_rules == ["rule1", "rule3", "rule3"]
    
def test_evaluation_result_with_empty_expected_and_actual():
    expected = []
    actual = []
    result = calculate_precision_recall(expected_rules=expected, actual_rules=actual)
    assert result.true_positives == []
    assert result.false_positives == []
    assert result.false_negatives == []
    assert result.precision == 1.0
    assert result.recall == 1.0
    
def test_calculate_evaluation_result():
    # Expected: SQL001, SEC004
    # Actual:   SQL001, STYLE002
    expected = ["SQL001", "SEC004"]
    actual = ["SQL001", "STYLE002"]
    result = calculate_precision_recall(expected_rules=expected, actual_rules=actual)
    assert result.true_positives == ["SQL001"]
    assert result.false_negatives == ["SEC004"]
    assert result.false_positives == ["STYLE002"]
    assert result.precision == 0.5
    assert result.recall == 0.5