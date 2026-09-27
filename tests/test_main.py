from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)

def test_run_evaluation():
    response = client.post(
        "/eval-runs",
        json={
            "id": "case-1",
            "expected_rules": ["SQL001", "SEC004"],
            "actual_rules": ["SQL001", "STYLE002"],
        },
    )
    
    assert response.status_code == 200
    result = response.json()
    
    assert result["true_positives"] == ["SQL001"]
    assert result["false_positives"] == ["STYLE002"]
    assert result["false_negatives"] == ["SEC004"]
    assert result["precision"] == 0.5
    assert result["recall"] == 0.5