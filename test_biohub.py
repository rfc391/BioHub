
import pytest
from biohub import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_biosafety(client):
    # Add a biosafety record
    response = client.post('/biosafety/', json={'id': 1, 'name': 'Biosafety Record 1'})
    assert response.status_code == 201

def test_biostasis(client):
    # Add a biostasis record
    response = client.post('/biostasis/', json={'id': 1, 'status': 'stable'})
    assert response.status_code == 201

def test_iot_monitoring(client):
    # Add IoT monitoring data
    response = client.post('/iot-monitoring/', json={'device_id': '123', 'temperature': 22.5})
    assert response.status_code == 201

def test_outbreaks(client):
    # Add outbreak data
    response = client.post('/outbreaks/', json={'id': 1, 'location': 'Region A'})
    assert response.status_code == 201

def test_incidents(client):
    # Add an incident report
    response = client.post('/incidents/', json={'id': 1, 'description': 'Incident A'})
    assert response.status_code == 201
