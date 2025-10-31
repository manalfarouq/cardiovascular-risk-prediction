
#* Ce fichier contient la logique CRUD, séparée des routes

from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


#! Étape 8 ---- Créer un patient (POST) ----
#! ===Endpoint POST===
def create_patient(db: Session, patient: schemas.PatientCreate):
    """Créer un nouveau patient dans la base de données.

    Cette fonction reçoit les données du patient envoyées par le client,
    les valide grâce au modèle Pydantic (PatientCreate),
    puis les enregistre dans la base via SQLAlchemy.
    Elle retourne ensuite le patient créé sous forme du modèle PatientRespond.

    POST → on ajoute des données.
    
    Args:
        db (Session): Session de base de données obtenue via get_db()
        patient (PatientCreate): Données du patient reçues du client (âge, genre, etc.)

    Raises:
        HTTPException: Si des valeurs invalides sont détectées (ex: âge négatif)

    Returns:
        models.Patient: Instance du patient nouvellement créée
    """
    
    db_patient = models.Patient(
        age=patient.age,
        gender=patient.gender,
        pressure_high=patient.pressure_high,
        pressure_low=patient.pressure_low,
        glucose=patient.glucose,
        kcm=patient.kcm,
        troponin=patient.troponin,
        impluse=patient.impluse,
    )
    db.add(db_patient)     #? ajoutent le patient dans la base
    db.commit()            #? valident les changements
    db.refresh(db_patient) #? récupèrent les infos mises à jour (avec l'ID créé).
    return db_patient


#! Étape 9 ---- Lire un patient par ID (GET) ----
#! ===Endpoint GET (ID)===
def get_patient(db: Session, patient_id: int):
    """Récupérer un patient spécifique depuis la base de données à partir de son ID.

    GET → on lit les données.

    Args:
        db (Session): Session de base de données obtenue via get_db()
        patient_id (int): Identifiant unique du patient à rechercher

    Raises:
        HTTPException: Si aucun patient ne correspond à l'ID fourni (erreur 404)

    Returns:
        models.Patient: Données du patient trouvé dans la base
    """
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


#! Étape 10 ---- Lister tous les patients (GET) ----
#! ===Endpoint GET (liste)===
def get_patients(db: Session):
    """Récupérer la liste complète des patients enregistrés dans la base de données.

    GET → on lit les données.

    Args:
        db (Session): Session de base de données obtenue via get_db()

    Returns:
        list[models.Patient]: Liste de tous les patients stockés dans la base de données
    """
    return db.query(models.Patient).all()
