from pathlib import Path
import pytest
from flask import jsonify
from unittest.mock import patch

import sys
import os
from pathlib import Path

# Asegúrate de que la raíz del proyecto esté en el PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Ahora, importa 'create_app' desde el archivo 'app.py' en la raíz
from app import create_app


# Fixture para crear el cliente de prueba de Flask
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Fixture para mockear la función fetch_data
@pytest.fixture
def mock_fetch_data():
    with patch('section1.fetch_data') as mock:
        # Simulamos una respuesta de ejemplo con algunos datos
        mock.return_value = [
            {
                "is_answered": True,
                "owner": {"reputation": 100},
                "view_count": 50,
                "creation_date": 1650000000,
            },
            {
                "is_answered": False,
                "owner": {"reputation": 150},
                "view_count": 25,
                "creation_date": 1700000000,
            },
        ]
        yield mock


# Prueba para el endpoint /api/section1/answered-status
def test_answered_status(client, mock_fetch_data):
    response = client.get('/api/section1/answered-status')
    print(response.data)  # Imprime la respuesta para depurar
    assert response.status_code == 200
    data = response.get_json()
    assert 'answered' in data
    assert 'unanswered' in data
    assert data['answered'] == 1
    assert data['unanswered'] == 1


# Prueba para el endpoint /api/section1/highest-reputation
def test_highest_reputation(client, mock_fetch_data):
    response = client.get('/api/section1/highest-reputation')
    print(response.data)  # Imprime la respuesta para depurar
    assert response.status_code == 200
    data = response.get_json()
    assert 'highest_reputation' in data
    assert data['highest_reputation']['owner']['reputation'] == 150


# Prueba para el endpoint /api/section1/lowest-views
def test_lowest_views(client, mock_fetch_data):
    response = client.get('/api/section1/lowest-views')
    print(response.data)  # Imprime la respuesta para depurar
    assert response.status_code == 200
    data = response.get_json()
    assert 'lowest_views' in data
    assert data['lowest_views']['view_count'] == 25


# Prueba para el endpoint /api/section1/oldest-newest
def test_oldest_newest(client, mock_fetch_data):
    response = client.get('/api/section1/oldest-newest')
    print(response.data)  # Imprime la respuesta para depurar
    assert response.status_code == 200
    data = response.get_json()
    assert 'oldest' in data
    assert 'newest' in data
    assert data['oldest']['creation_date'] == 1650000000
    assert data['newest']['creation_date'] == 1700000000


# Prueba para el endpoint /api/section1/least-viewed
def test_least_viewed(client, mock_fetch_data):
    response = client.get('/api/section1/least-viewed')
    print(response.data)  # Imprime la respuesta para depurar
    assert response.status_code == 200
    data = response.get_json()
    assert 'least_viewed' in data
    assert data['least_viewed']['view_count'] == 25
