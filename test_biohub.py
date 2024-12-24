
import pytest
from biohub import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()['message'] == "Welcome to BioHub - Revolutionizing Biosafety and Monitoring!"

def test_biosafety(client):
    # Add a biosafety record
    response = client.post('/biosafety', json={'id': 1, 'name': 'Biosafety Record 1'})
    assert response.status_code == 201
    assert response.get_json()['message'] == "Biosafety record added!"
    
    # Get all biosafety records
    response = client.get('/biosafety')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_biostasis(client):
    # Add a biostasis record
    response = client.post('/biostasis', json={'id': 1, 'status': 'stable'})
    assert response.status_code == 201
    assert response.get_json()['message'] == "Biostasis record added!"
    
    # Get all biostasis records
    response = client.get('/biostasis')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_iot_monitoring(client):
    # Add IoT monitoring data
    response = client.post('/iot-monitoring', json={'device_id': '123', 'temperature': 22.5})
    assert response.status_code == 201
    assert response.get_json()['message'] == "IoT Monitoring data added!"
    
    # Get all IoT monitoring data
    response = client.get('/iot-monitoring')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_outbreaks(client):
    # Add outbreak data
    response = client.post('/outbreaks', json={'id': 1, 'location': 'Region A'})
    assert response.status_code == 201
    assert response.get_json()['message'] == "Outbreak data added!"
    
    # Get all outbreak data
    response = client.get('/outbreaks')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_incidents(client):
    # Add an incident report
    response = client.post('/incidents', json={'id': 1, 'description': 'Incident A'})
    assert response.status_code == 201
    assert response.get_json()['message'] == "Incident report added!"
    
    # Get all incident reports
    response = client.get('/incidents')
    assert response.status_code == 200
    assert len(response.get_json()) == 1
