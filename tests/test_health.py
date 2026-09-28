from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json() == {
        "service": "AI Prediction Service",
        "version": "1.0.0",
    }

def test_predict_approved():
    response = client.post(
        "/predict",
        json={
            "age": 35,
            "income": 60000,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "prediction": "approved",
        "score": 0.90,
    }

def test_predict_review():
    response = client.post(
        "/predict",
        json={
            "age": 35,
            "income": 40000,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "prediction": "review",
        "score": 0.60,
    }