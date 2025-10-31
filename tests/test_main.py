
import pytest
from fastapi.testclient import TestClient
# from main import app
from fastapi import FastAPI

app = FastAPI
client = app

def test_prediction_risk_status_code(): 
   data={"prénom": "khadija",
       "age": 55, 
       "income": 40000,
       "gender": "male"}
   response= client.post("/predict_risk", json=data)
   assert response.status_code==200
   json_data =response.json()
   assert json_data["prediction"] in ["low", "high"]
   
   
def test_predict_risk_invalid_data():
        invalid_data = {"prenom": 234, 
                    #   "age" manquant, 
                    "income": 40000,
                    "gender": "male"
                    }
        response=client.post("/predict_risk", json=invalid_data)
        assert response.status_code==422
