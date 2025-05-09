import pytest
from flask_app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'Welcome to the Flask API' in data['message']

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data

def test_api_data_route(client):
    response = client.get('/api-data')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert len(data['data']) >= 3