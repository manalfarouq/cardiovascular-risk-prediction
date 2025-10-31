
#* Ce fichier gère la connexion à la base de données


#! Etape 3 ---- Créer la base de données ----
# === SQLAlchemy === permet d'écrire du code Python au lieu de requêtes SQL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data/patients.db" #? patients.db(fichier de la base) → sera créé automatiquement dans ton dossier
engine = create_engine(DATABASE_URL)          #? engine = moteur de communication entre ton code et la base

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()                     #? classe mère pour définir des tables (modèles de données).

#? Cela permet de créer une connexion temporaire à la base (appelée une “session”).
#? Tu l'ouvriras chaque fois que tu veux lire ou écrire des données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#! Etape 5 ---- Creer la table dans la base ----
Base.metadata.create_all(bind=engine)
#* => FastAPI va demander à SQLAlchemy de créer la table items dans ton fichier patient.db


#! Etape 6 ---- Connexion à la base ----
def get_db():
    db = SessionLocal()                       #? ouvre la connexion à la base
    try:
        yield db                              #? donne la connexion à l'API pour exécuter une action (yield la donne temporairement à FastAPI)
    finally:
        db.close()                            #? ferme la connexion après utilisation
#* FastAPI utilise Depends(get_db) pour accéder à la base sans la laisser ouverte
