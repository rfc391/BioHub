
import pytest
from biohub import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()['message'] == "BioHub API is running"

def test_register_login(client):
    # Register user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 201

    # Login user
    response = client.post('/api/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert 'Login successful' in response.get_json()['message']
