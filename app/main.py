
#! Etape 1 --- Importation modules et classes necessaires ---
"""
    1==> FastAPI → créer l'API web

    2==> Uvicorn → faire tourner le serveur local

    3==> SQLAlchemy → communiquer avec la base de données

    4==> Pydantic → valider les données envoyées par l'utilisateur
    
    FastAPI reçoit des données ⮕ Pydantic les valide ⮕ SQLAlchemy les enregistre dans la base
    
    ==============================================================================================
    
    Utilisateur → (envoie JSON)
        ↓
    FastAPI → reçoit requête
        ↓
    Pydantic → valide les données
        ↓
    SQLAlchemy → traduit en requêtes SQL
        ↓
    Base de données SQLite → stocke les patients
        ↓
    SQLAlchemy → récupère les résultats
        ↓
    Pydantic → formate les données de sortie
        ↓
    FastAPI → renvoie la réponse au client

    """
    
# === FastAPI ===
from fastapi import FastAPI ,Depends                                 #? crée des routes (endpoints) de l'application web

# === SQLAlchemy ===
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# === schemas.py ===
from .schemas import *

# === models.py ===
from .models import predict_risk

#* Crée toutes les tables définies dans les modèles SQLAlchemy
#* - Base.metadata contient la "structure" de toutes les tables (Patient)
#* - bind=engine indique la base de données dans laquelle créer les tables (SQLite)
#* - Si les tables existent déjà, rien ne se passe
models.Base.metadata.create_all(bind=engine)



#! Etape 2 ---- Créer l'application FastAPI ----
app = FastAPI(title="API de Prédiction de Risque Cardiovasculaire")  #? Ça crée l'application web

# === Endpoint racine ===
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Prédiction de Risque Cardiovasculaire!"}

#! Etape 8 ---- Creer un patient (POST) ---- 
# ===Endpoint POST===
@app.post("/patients/", response_model=schemas.PatientRespond)
async def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

#! Etape 9 ---- Lire un patient par ID ---- 
# ===Endpoint GET (ID)===
@app.get("/patients/{patient_id}", response_model=schemas.PatientRespond)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    return crud.get_patient(db, patient_id=patient_id)

#! Étape 10 ---- Lister tous les patients (GET) ---- 
# ===Endpoint GET (liste)===
@app.get("/patients/", response_model=list[schemas.PatientRespond])
async def list_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)


# === Endpoint de prédiction ===
@app.post("/predict", response_model=PredictionResponse)
async def predict(data: PatientRespond):
    features = [
        data.age, data.gender, data.pressure_high, data.pressure_low,
        data.glucose, data.kcm, data.troponin, data.impluse
    ]
    prediction = predict_risk(features)
    return {"prediction": prediction}
