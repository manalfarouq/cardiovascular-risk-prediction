
#* Ce fichier contient les classes qui représentent tes tables.

from sqlalchemy import Column, Integer
from .database import Base

# === joblib ===
import joblib
import numpy as np
import pandas as pd
import os

#! Etape 4 ---- Definir un 'modele' ----=> c'est une classe qui décrit comment sera ta table dans la base
from sqlalchemy import Column, Integer, Float

class Patient(Base):                          #? Cette classe = table dans la base
    __tablename__ = "patients" 
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)                  #? 0=femme, 1=homme
    pressure_high = Column(Float)
    pressure_low = Column(Float)
    glucose = Column(Float)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Float)


# === Charger le modèle ===
def load_model():
    # Trouve le dossier courant du fichier models.py
    base_dir = os.path.dirname(__file__)
    
    # Construit le chemin absolu vers src/best_model_rf.pkl
    model_path = os.path.join(base_dir, "../src/best_model_rf.pkl")
    model_path = os.path.abspath(model_path)  # pour éviter les erreurs de chemin relatif
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modèle introuvable à : {model_path}")
    
    return joblib.load(model_path)

model = load_model()                   #? Charger le modèle une seule fois (singleton)


# === Endpoint de prédiction ===
def predict_risk(features):
    """
    Prend une liste de valeurs et renvoie la prédiction du modèle
    """
    columns = [
        "age",
        "pressurehight",  # ← Changed to match the model's expected column name
        "pressurelow",
        "glucose",
        "kcm",
        "troponin",
        "impluse"
    ]
    
    # On transforme la liste en DataFrame (comme pendant l'entraînement)
    df = pd.DataFrame([features], columns=columns)
    prediction = model.predict(df)[0]
    return int(prediction)