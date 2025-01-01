
import pytest
from biohub import app, get_db_connection

@pytest.fixture
def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS biosafety (id INTEGER PRIMARY KEY, record TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS biostasis (id INTEGER PRIMARY KEY, record TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS iot (id INTEGER PRIMARY KEY, record TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS outbreaks (id INTEGER PRIMARY KEY, record TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS incidents (id INTEGER PRIMARY KEY, record TEXT NOT NULL);
    ''')
    conn.commit()
    yield
    cursor.executescript('''
    DROP TABLE IF EXISTS biosafety;
    DROP TABLE IF EXISTS biostasis;
    DROP TABLE IF EXISTS iot;
    DROP TABLE IF EXISTS outbreaks;
    DROP TABLE IF EXISTS incidents;
    ''')
    conn.commit()
    conn.close()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_biosafety(setup_database, client):
    response = client.post('/biosafety/', json={'id': 1, 'name': 'Biosafety Record 1'})
    assert response.status_code == 201
