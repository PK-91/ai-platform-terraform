from fastapi import FastAPI

from app.models import PredictionRequest, PredictionResponse
from app.services.prediction_service import predict


app = FastAPI(title="AI Prediction Service")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/info")
def application_info():
    return {
        "service": "AI Prediction Service",
        "version": "1.0.0",
    }


@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    prediction, score = predict(
        request.age,
        request.income,
    )

    return PredictionResponse(
        prediction=prediction,
        score=score,
    )