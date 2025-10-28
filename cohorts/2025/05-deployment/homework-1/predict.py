import pickle
from typing import Literal
from pydantic import BaseModel, Field


from fastapi import FastAPI
import uvicorn





# url = "YOUR_URL"
# client = {
#     "lead_source": "organic_search",
#     "number_of_courses_viewed": 4,
#     "annual_income": 80304.0
# }
# requests.post(url, json=client).json()

class Customer(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool


app = FastAPI(title="customer-churn-prediction")

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer.model_dump())

    return PredictResponse(
        churn_probability=prob,
        churn=prob >= 0.5
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)