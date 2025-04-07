from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")


# Load the Hugging Face sentiment analysis pipeline
pipe = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = pipe(input.text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }
