
#* Ce fichier contient les classes qui représentent tes tables.

from sqlalchemy import Column, Integer
from .database import Base

# === joblib ===
import joblib
import numpy as np

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
    model_path = "../src/best_model_rf.pkl"  
    model = joblib.load(model_path)
    return model

model = load_model()                   #? Charger le modèle une seule fois (singleton)


# === Endpoint de prédiction ===
def predict_risk(data: list):
    """
    data: liste de valeurs [age, gender, pressure_high, pressure_low, glucose, kcm, troponin, impulse]
    Retourne la prédiction.
    """
    features = np.array([data])        #? transformer en tableau 2D pour sklearn

    # Prédiction avec le modèle
    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }