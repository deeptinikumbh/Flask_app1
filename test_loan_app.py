import pytest
from mini_api import app

#make something that minics the server
@pytest.fixture
def client():
    return app.test_client()

def test_hello_world(client):
    res=client.get('/')
    assert res.json=={"Message":"Hello Welcome to loan prediction system!!!"}

def test_hello_ping(client):
    res=client.get('/ping')
    assert res.json=={"message":"Hello Pong"}


def test_predict(client):
    test_data={
"Gender": "Male",
"Married": "No",
"ApplicantIncome": 10000000,
"LoanAmount": 5000,
"Credit_History": 1.0
}
    res=client.post("/predict",json=test_data)
    assert res.json=={"loan_approval_status": "Approved"}
