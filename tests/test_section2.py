import pytest
from app import create_app
from models.models import db, Aerolinea, Aeropuerto, Vuelo, Movimiento



@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_aeropuerto_mayor_movimiento(client):
    # Hacer una solicitud GET a la ruta para obtener el aeropuerto con mayor movimiento
    response = client.get('/api/section2/aeropuerto-mayor-movimiento')

    assert response.status_code == 200
    data = response.get_json()
    assert 'aeropuerto' in data
    assert 'cantidad_vuelos' in data

def test_aerolinea_mayor_vuelos(client):
    # Hacer una solicitud GET a la ruta para obtener la aerolínea con mayor cantidad de vuelos
    response = client.get('/api/section2/aerolinea-mayor-vuelos')

    assert response.status_code == 200
    data = response.get_json()
    assert 'aerolinea' in data
    assert 'cantidad_vuelos' in data

def test_dia_mayor_vuelos(client):
    # Hacer una solicitud GET a la ruta para obtener el día con mayor número de vuelos
    response = client.get('/api/section2/dia-mayor-vuelos')

    assert response.status_code == 200
    data = response.get_json()
    assert 'dia' in data
    assert 'cantidad_vuelos' in data

def test_aerolineas_mas_de_2_vuelos(client):
    # Hacer una solicitud GET a la ruta para obtener aerolíneas con más de 2 vuelos por día
    response = client.get('/api/section2/aerolineas-mas-de-2-vuelos')

    # Aceptar tanto el código de estado 200 como el 404
    assert response.status_code in [200, 404]

    # Si la respuesta es 200, verificar los datos
    if response.status_code == 200:
        data = response.get_json()
        assert isinstance(data, list)  # Verifica que la respuesta sea una lista
        for item in data:
            assert 'aerolinea' in item
            assert 'dia' in item
            assert 'cantidad_vuelos' in item
    # Si la respuesta es 404, verificar que se reciba un mensaje adecuado
    elif response.status_code == 404:
        data = response.get_json()
        assert 'message' in data
        assert data['message'] == 'No se encontraron aerolíneas con más de 2 vuelos por día'
