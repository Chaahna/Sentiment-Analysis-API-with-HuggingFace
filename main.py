# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Loads the sentiment analysis model once when the server starts
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Defines the input structure with Pydantic for data validation
class TextInput(BaseModel):
    text: str

# Defines the POST route
@app.post("/predict")
def predict_sentiment(data: TextInput):
    # Uses the classifier to analyze the text
    result = classifier(data.text)[0]
    # Returns the label and confidence score
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }
