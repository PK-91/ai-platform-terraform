def predict(age: int, income: float) -> tuple[str, float]:
    if income >= 50000:
        return "approved", 0.90

    return "review", 0.60