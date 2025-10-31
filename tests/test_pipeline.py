
import pytest
from fastapi.testclient import TestClient
from main import app
# from app.main import app

client = TestClient(app)

def test_home(): 
    response= client.get("/")
    assert response.status_code==200
    assert response.json()== {"message" : "Bienvenue sur l'API de Prédiction de Risque Cardiovasculaire!"}

def test_create_patient(): 
    payload={ 
        "age":50,
        "gender":0,
        "pressure_high":130, 
        "pressure_low":85,
        "glucose":5.0,
        "kcm":170,
        "troponin":0.02,
        "impluse": 72
    }
    response=client.post("/patients/", json=payload)
    assert response.status_code==200
    data=response.json()
    assert "id" in data
    assert data["age"]==50
    assert data ["gender"]==0

def test_list_patients():
    response= client.get("/patients/")
    assert response.status_code==200
    data=response.json()
    


# def test_root():
#     response = client.get("/fatima")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello My world"}

# def test_create_and_list_patient():
#     patient_data = {
#         "name": "John",
#         "age": 50,
#         "gender": "male",
#         "cholesterol": 200.5,
#         "blood_pressure": 130
#     }
#     response = client.post("/patients", json=patient_data)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "John"

#     response = client.get("/patients")
#     assert response.status_code == 200
#     assert any(p["name"]=="John" for p in response.json())

# def test_predict_risk():
#     patient_data = {
#         "name": "Alice",
#         "age": 60,
#         "gender": "female",
#         "cholesterol": 220,
#         "blood_pressure": 140
#     }
#     response = client.post("/predict_risk", json=patient_data)
#     assert response.status_code == 200
#     assert "risk_score" in response.json()

