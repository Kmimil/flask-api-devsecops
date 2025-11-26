from app import app
import pytest
def test_home_route():
    """Test de la route principale"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data

def test_health_route():
    """Test de la route health"""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info_route():
    """Test de la route info"""
    client = app.test_client()
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'institution' in data
    assert 'ENSAJ' in data['institution']
