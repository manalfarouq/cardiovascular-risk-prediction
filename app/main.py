from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Création de l'application
app = FastAPI(title="API de Prédiction - Modèle Machine Learning")

# === Définition du format d'entrée ===
class InputData(BaseModel):
    age: int
    gender: int
    status: int
    pressure_high: int
    pressure_low: int
    glucose: float
    kcm : float
    troponin : float
    impluse : int

# === Chargement du modèle ===
def load_model():
    model_path = "model dialna."  
    model = joblib.load(model_path)
    return model

model = load_model()

# === Endpoint racine ===
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de prédiction de risque cardiovasculaire"}

# === Endpoint de prédiction ===
@app.post("/predict")
def predict(data: InputData):
    # Transformation des données reçues en tableau numpy
    features = np.array([[ 
        data.age, 
        data.gender, 
        data.status, 
        data.pressure_high, 
        data.pressure_low, 
        data.glucose, 
        data.kcm, 
        data.troponin, 
        data.impulse
    ]])

    # Prédiction avec le modèle
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].tolist() if hasattr(model, "predict_proba") else None

    return {
        "prediction": int(prediction),
        "probabilities": probability
    }
