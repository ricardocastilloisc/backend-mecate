from models.models import db, Aerolinea, Aeropuerto, Movimiento, Vuelo
from datetime import datetime

def insertar_datos():
    aerolineas = [
        Aerolinea(id_aerolinea=1, nombre_aerolinea='Volaris'),
        Aerolinea(id_aerolinea=2, nombre_aerolinea='Aeromar'),
        Aerolinea(id_aerolinea=3, nombre_aerolinea='Interjet'),
        Aerolinea(id_aerolinea=4, nombre_aerolinea='Aeromexico')
    ]
    aeropuertos = [
        Aeropuerto(id_aeropuerto=1, nombre_aeropuerto='Benito Juarez'),
        Aeropuerto(id_aeropuerto=2, nombre_aeropuerto='Guanajuato'),
        Aeropuerto(id_aeropuerto=3, nombre_aeropuerto='La paz'),
        Aeropuerto(id_aeropuerto=4, nombre_aeropuerto='Oaxaca')
    ]
    movimientos = [
        Movimiento(id_movimiento=1, descripcion='Salida'),
        Movimiento(id_movimiento=2, descripcion='Llegada')
    ]
    vuelos = [
        Vuelo(id_aerolinea=1, id_aeropuerto=1, id_movimiento=1, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=2, id_aeropuerto=1, id_movimiento=1, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=3, id_aeropuerto=2, id_movimiento=2, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=4, id_aeropuerto=3, id_movimiento=2, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=1, id_aeropuerto=3, id_movimiento=2, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=2, id_aeropuerto=1, id_movimiento=1, dia=datetime.strptime('2021-05-02', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=2, id_aeropuerto=3, id_movimiento=1, dia=datetime.strptime('2021-05-04', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=3, id_aeropuerto=4, id_movimiento=1, dia=datetime.strptime('2021-05-04', '%Y-%m-%d').date()),
        Vuelo(id_aerolinea=3, id_aeropuerto=4, id_movimiento=1, dia=datetime.strptime('2021-05-04', '%Y-%m-%d').date())
    ]

    db.session.add_all(aerolineas + aeropuertos + movimientos + vuelos)
    db.session.commit()
