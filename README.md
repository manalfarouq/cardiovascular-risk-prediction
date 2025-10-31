#  API de Prédiction du Risque Cardio-vasculaire
### *Auteur :* __Asmae, __Manal,__MACHAY Fatima__  
### *Date :* __2025-10-31__  
### *Objectif :*  
Développer une **API complète** basée sur FastAPI, connectée à une base de données SQLite et intégrant un modèle de Machine Learning pour **prédire le risque de maladies cardio-vasculaires** à partir des données cliniques d’un patient.

----------------------------------------------------------------------------------------------------

##  Présentation du Projet :

Les **maladies cardio-vasculaires** sont la principale cause de mortalité dans le monde, responsables de près de **17,9 millions de décès par an**.  
Ce projet vise à créer un outil d’aide à la décision médicale permettant d’estimer le risque de développer une maladie cardiaque, à partir d’informations comme l’âge, le cholestérol, la tension artérielle ou les habitudes de vie.

L’API fournit des fonctionnalités permettant d’ajouter des patients, de lister les enregistrements et de prédire le score de risque cardio-vasculaire via un modèle entraîné avec **Scikit-learn**.

----------------------------------------------------------------------------------------------------

##  Table des Matières :

- [Gestion de Projet](#gestion-de-projet)
- [Architecture du Projet](#architecture-du-projet)
- [Installation](#installation)
- [Base de Données](#base-de-données)
- [Machine Learning](#machine-learning)
- [Endpoints de l’API](#endpoints-de-lapi)
- [Tests Unitaires](#tests-unitaires)
- [Documentation](#documentation)
- [Exécution du Projet](#exécution-du-projet)
- [Contribuer](#contribuer)
- [Contact](#contact)

----------------------------------------------------------------------------------------------------

##  Gestion de Projet :

Travail en **trinôme** avec une répartition claire des rôles :

| Rôle | Responsabilités principales |
|------|------------------------------|
| **Développeur Backend** | Structure FastAPI, intégration SQLite, création des endpoints CRUD |
| **Développeur IA/Data** | Nettoyage du dataset, entraînement du modèle ML, intégration du modèle dans FastAPI |
| **Documentation & Tests** | Rédaction de la documentation technique (README, Swagger), création des tests unitaires avec pytest et validation du bon fonctionnement global de l’API. |

**Collaboration via GitHub :**
- Branche principale : `main`  
- Branche API : `feature/api`  
- Branche Machine Learning : `feature/ml`
- Branche Machine Learning : `feature/test`


----------------------------------------------------------------------------------------------------


##  Architecture du Projet :

project/
│
├── main.py
├── models/
│ ├── patient.py
│ └── init.py
├── routes/
│ ├── patients.py
│ ├── prediction.py
│ └── init.py
├── database.py
├── ml/
│ ├── train_model.py
│ ├── model.joblib
│ └── init.py
├── tests/
│ └── test_api.py
├── requirements.txt
└── README.md

yaml
Copier le code

---

##  Installation :

1. **Cloner le dépôt :**
   ```bash
   git clone 
   [git clone](https://github.com/manalfarouq/cardiovascular-risk-prediction.git)
   cd projet-cardio
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Dépendances principales :

- fastapi
- uvicorn
- sqlalchemy
- pandas
- scikit-learn
- joblib
- pytest
- numpy
- matplotlib
- seaborn
- pytest
- pydantic


## Base de Données :
Le projet utilise une base SQLite pour stocker les informations des patients.
Les données sont gérées via SQLAlchemy et validées par Pydantic avant insertion.

## Machine Learning :
Le modèle prédictif est basé sur un pipeline Scikit-learn :

python
Copier le code
Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
Étapes principales :
Chargement et nettoyage du dataset (via pandas)

Encodage et normalisation des données

Séparation X / y et train / test

Entraînement du modèle

Sauvegarde avec :

python
Copier le code
joblib.dump(model, "model.joblib")


## Endpoints de l’API :
Méthode	Endpoint	Description
POST	/patients	Ajouter un patient
GET	/patients	Lister les patients
POST	/predict_risk	Prédire le risque cardio-vasculaire

Exemple JSON :
json
Copier le code
{
  "age": 54,
  "sex": "male",
  "cholesterol": 230,
  "blood_pressure": 140,
  "smoking": 1
}
## Tests Unitaires :
Les tests sont réalisés avec pytest et TestClient de FastAPI.

Exemple :
python
Copier le code
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_risk():
    response = client.post("/predict_risk", json={"age": 45, "sex": "male", "cholesterol": 210})
    assert response.status_code == 200
Les tests vérifient :

la validité du status_code

la cohérence des entrées/sorties JSON

## Documentation :
FastAPI fournit une documentation interactive intégrée :

Swagger UI 👉 http://127.0.0.1:8000/docs

ReDoc 👉 http://127.0.0.1:8000/redoc

## Exécution du Projet :
Lancer le serveur local :

bash
Copier le code
uvicorn main:app --reload
L’API sera disponible sur :
👉 http://127.0.0.1:8000

## Contribuer :
Les contributions sont les bienvenues !

Forkez le dépôt

Créez une nouvelle branche (feature/ma-fonctionnalite)

Apportez vos modifications

Soumettez une pull request

## Contact :
👩‍💻 Fatima MACHAY
📧 fatimamachay5@gmail.com