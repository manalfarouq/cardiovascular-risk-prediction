
#! Etape 1 --- Importation modules et classes necessaires ---
"""
    1==> FastAPI → créer l'API web

    2==> Uvicorn → faire tourner le serveur local

    3==> SQLAlchemy → communiquer avec la base de données

    4==> Pydantic → valider les données envoyées par l'utilisateur
    
    """

from fastapi import FastAPI ,HTTPException
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

#! Etape 2 ---- Créer l'application FastAPI ----
app = FastAPI(title="API de Prédiction de Risque Cardiovasculaire")  #? Ça crée l'application web


#! Etape 3 ---- Créer la base de données ----

DATABASE_URL = DATABASE_URL = "sqlite:///./data/patients.db" #? patients.db(fichier de la base) → sera créé automatiquement dans ton dossier
engine = create_engine(DATABASE_URL) #? engine = moteur de communication entre ton code et la base

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#? Cela permet de créer une connexion temporaire à la base (appelée une “session”).
#? Tu l'ouvriras chaque fois que tu veux lire ou écrire des données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#! Etape 4 ---- Definir un 'modele' ----=> c'est une classe qui décrit comment sera ta table dans la base
from sqlalchemy import Column, Integer, Float

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)           # 0=femme, 1=homme
    pressure_high = Column(Float)
    pressure_low = Column(Float)
    glucose = Column(Float)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Float)



#! Etape 5 ---- Creer la table dans la base ----
Base.metadata.create_all(bind=engine)
#* => FastAPI va demander à SQLAlchemy de créer la table items dans ton fichier test.db

#! Etape 6 ---- Connexion à la base ----
def get_db():
    db = SessionLocal() #? ouvre la connexion
    try:
        yield db #? donne la connexion à l'API pour exécuter une action
    finally:
        db.close() #? ferme la connexion après utilisation


#! Etape 7 ---- Modele Pydantic ----
#* Entrée (ce que l'utilisateur envoie) :
from pydantic import BaseModel
class PatientCreate(BaseModel):
    age: int
    gender: int
    pressure_high: float
    pressure_low: float
    glucose: float
    kcm: float
    troponin: float
    impluse: float
    

#* Sortie (ce que l'API renvoie) :
class PatientRespond(BaseModel):
    id: int
    age: int
    gender: int
    pressure_high: float
    pressure_low: float
    glucose: float
    kcm: float
    troponin: float
    impluse: float
    class Config:
        orm_mode = True  # permet la compatibilité ORM <=> Pydantic


#! Etape 8 ---- Creer un patient (POST) ----
from fastapi import Depends
from sqlalchemy.orm import Session

@app.post("/patients/", response_model=PatientRespond)
async def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    
    # Vérification basique
    if patient.age < 0 or patient.glucose < 0:
        raise HTTPException(status_code=400, detail="Valeurs invalides (négatives)")
    
    db_patient = Patient(
        age=patient.age,
        gender=patient.gender,
        pressure_high=patient.pressure_high,
        pressure_low=patient.pressure_low,
        glucose=patient.glucose,
        kcm=patient.kcm,
        troponin=patient.troponin,
        impluse=patient.impluse,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

#! Etape 9 ---- Lire un patient (GET) ---- Recuperer un patient par id
from fastapi import HTTPException

@app.get("/patients/{patient_id}", response_model=PatientRespond)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


#! Étape 10 ---- Endpoint GET (liste de tous les patients) ----

@app.get("/patients/", response_model=list[PatientRespond])
async def list_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients


#! Étape 11 ---- Endpoint racine ----

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Prédiction !"}

# # Création de l'application
# app = FastAPI(title="API de Prédiction - Modèle Machine Learning")

# # === Définition du format d'entrée ===
# class InputData(BaseModel):
#     age: int
#     gender: int
#     status: int
#     pressure_high: int
#     pressure_low: int
#     glucose: float
#     kcm : float
#     troponin : float
#     impluse : int

# # === Chargement du modèle ===
# def load_model():
#     model_path = "model dialna."  
#     model = joblib.load(model_path)
#     return model

# model = load_model()

# # === Endpoint racine ===
# @app.get("/")
# def home():
#     return {"message": "Bienvenue sur l'API de prédiction de risque cardiovasculaire"}

# # === Endpoint de prédiction ===
# @app.post("/predict")
# def predict(data: InputData):
#     # Transformation des données reçues en tableau numpy
#     features = np.array([[ 
#         data.age, 
#         data.gender, 
#         data.status, 
#         data.pressure_high, 
#         data.pressure_low, 
#         data.glucose, 
#         data.kcm, 
#         data.troponin, 
#         data.impulse
#     ]])

#     # Prédiction avec le modèle
#     prediction = model.predict(features)[0]
#     probability = model.predict_proba(features)[0].tolist() if hasattr(model, "predict_proba") else None

#     return {
#         "prediction": int(prediction),
#         "probabilities": probability
#     }
