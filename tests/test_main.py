from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)
def test_status_code():
    response = client.get('/patients/predict_risk')
    # print(response.status_code)
    assert response.status_code == 200