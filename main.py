import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from transformers import pipeline
from models import TextPayload, PredictionResponse

# Initialize a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis Microservice",
    description="A simple microservice to analyze sentiment using a pre-trained Hugging Face model."
)

# Mount static files (if you have HTML frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the sentiment analysis model
try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    classifier = None

# Root endpoint
@app.get("/", response_class=HTMLResponse, tags=["UI"])
async def read_root():
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Bienvenue ! Allez sur /gradio pour tester l'application 🙂</h1>"

# Health check
@app.get("/health", tags=["Monitoring"])
async def health_check():
    if classifier:
        return {"status": "ok", "message": "Service is healthy and model is loaded."}
    else:
        raise HTTPException(status_code=503, detail="Service is unhealthy: Model not loaded.")

# Prediction API
@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_sentiment(payload: TextPayload, request: Request):
    if not classifier:
        raise HTTPException(status_code=503, detail="Model not ready. Please try again later.")
        
    text_to_analyze = payload.text.strip()
    if not text_to_analyze:
        logger.warning("Empty text received.")
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
        
    try:
        prediction = classifier(text_to_analyze)[0]
        return PredictionResponse(sentiment=prediction['label'], score=prediction['score'])
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")

