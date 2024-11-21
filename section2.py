from flask import Blueprint
from flask_restx import Api, Resource
from models.models import db, Aerolinea, Aeropuerto, Movimiento, Vuelo  # Asegúrate de importar db y tus modelos de Aeropuerto, Aerolinea, y Vuelo

# Definir el Blueprint
section2_blueprint = Blueprint("section2", __name__)

# Crear la API a partir del Blueprint
api = Api(
    section2_blueprint,
    version='1.0', 
    title='BackEnd Ejercicio 2 API',
    description='Documentación de la API para el Ejercicio 2 del reto técnico',
    doc='/swagger')  # `/swagger` es donde estará disponible la documentación de la API


# Consulta 1: ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?
@api.route('/aeropuerto-mayor-movimiento')
class AeropuertoMayorMovimiento(Resource):
    @api.doc(description="Obtiene el nombre del aeropuerto con mayor cantidad de vuelos realizados durante el año.")
    def get(self):
        query = db.session.query(
            Aeropuerto.nombre_aeropuerto, db.func.count(Vuelo.id_vuelo).label('cantidad_vuelos')
        ).join(Vuelo, Vuelo.id_aeropuerto == Aeropuerto.id_aeropuerto).group_by(Aeropuerto.id_aeropuerto).order_by(db.func.count(Vuelo.id_vuelo).desc()).first()

        return {'aeropuerto': query.nombre_aeropuerto, 'cantidad_vuelos': query.cantidad_vuelos}

# Consulta 2: ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?
@api.route('/aerolinea-mayor-vuelos')
class AerolineaMayorVuelos(Resource):
    @api.doc(description="Obtiene el nombre de la aerolínea con el mayor número de vuelos realizados durante el año.")
    def get(self):
        query = db.session.query(
            Aerolinea.nombre_aerolinea, db.func.count(Vuelo.id_vuelo).label('cantidad_vuelos')
        ).join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea).group_by(Aerolinea.id_aerolinea).order_by(db.func.count(Vuelo.id_vuelo).desc()).first()

        return {'aerolinea': query.nombre_aerolinea, 'cantidad_vuelos': query.cantidad_vuelos}


# Consulta 3: ¿En qué día se han tenido mayor número de vuelos?
@api.route('/dia-mayor-vuelos')
class DiaMayorVuelos(Resource):
    @api.doc(description="Obtiene el día con el mayor número de vuelos realizados durante el año.")
    def get(self):
        query = db.session.query(
            Vuelo.dia, db.func.count(Vuelo.id_vuelo).label('cantidad_vuelos')
        ).group_by(Vuelo.dia).order_by(db.func.count(Vuelo.id_vuelo).desc()).first()

        if query:
            return {'dia': query.dia.strftime('%Y-%m-%d'), 'cantidad_vuelos': query.cantidad_vuelos}
        else:
            return {'message': 'No se encontraron vuelos'}, 404
    

# Consulta 4: ¿Cuáles son las aerolíneas que tienen más de 2 vuelos por día?
@api.route('/aerolineas-mas-de-2-vuelos')
class AerolineasMasDe2Vuelos(Resource):
    @api.doc(description="Obtiene las aerolíneas que tienen más de 2 vuelos en un solo día.")
    def get(self):
        # Contamos los vuelos por aerolínea y día
        query = db.session.query(
            Aerolinea.nombre_aerolinea, Vuelo.dia, db.func.count(Vuelo.id_vuelo).label('cantidad_vuelos')
        ).join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea) \
         .group_by(Aerolinea.id_aerolinea, Vuelo.dia) \
         .having(db.func.count(Vuelo.id_vuelo) > 2) \
         .order_by(db.func.count(Vuelo.id_vuelo).desc()).all()

        # Devolver las aerolíneas con más de 2 vuelos por día
        result = []
        for item in query:
            result.append({
                'aerolinea': item.nombre_aerolinea,
                'dia': item.dia.strftime('%Y-%m-%d'),
                'cantidad_vuelos': item.cantidad_vuelos
            })

        if result:
            return result
        else:
            return {'message': 'No se encontraron aerolíneas con más de 2 vuelos por día'}, 404
