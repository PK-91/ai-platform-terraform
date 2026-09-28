from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    age: int = Field(gt=0, le=120)
    income: float = Field(gt=0)


class PredictionResponse(BaseModel):
    prediction: str
    score: float