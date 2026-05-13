import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from inference import batch_predict, predict_price
from prometheus_client import start_http_server
from prometheus_fastapi_instrumentator import Instrumentator
from schemas import HousePredictionRequest, PredictionResponse


# Initialize FastAPI app with metadata
app = FastAPI(
    title="House Price Prediction API",
    description=(
        "An API for predicting house prices based on various features. "
    ),
    version="1.0.0"
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add Prometheus instrumentation
Instrumentator().instrument(app).expose(app)


# Start Prometheus metric server in a separate thread on port 9100
prometheus_thread = threading.Thread(target=lambda: start_http_server(port=9100))
prometheus_thread.start()


# Health check endpoint
@app.get("/health", response_model=dict)
async def health_check():
    return {"status": "healthy", "model_loaded": True}


# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: HousePredictionRequest):
    return predict_price(request)


# Batch prediction endpoint
@app.post("/batch-predict", response_model=list)
async def batch_predict_endpoint(requests: list[HousePredictionRequest]):
    return batch_predict(requests)
