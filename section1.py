from flask import Blueprint, jsonify
from flask_restx import Api, Resource
from services.stackexchange_service import fetch_data

# Crear el blueprint para la sección 1
section1_blueprint = Blueprint("section1", __name__)

# Crear la instancia de Api dentro del blueprint sin un namespace
api = Api(section1_blueprint,
          version='1.0', 
          title='BackEnd Ejercicio 1 API',
          description='Documentación de la API para el Ejercicio 1 del reto técnico',
          doc='/swagger')  # `/swagger` es donde estará disponible la documentación de la API

# 1. Obtener el número de respuestas contestadas y no contestadas
@api.route('/answered-status')
class AnsweredStatus(Resource):
    def get(self):
        """
        Obtener el número de respuestas contestadas y no contestadas
        """
        data = fetch_data()
        answered = sum(1 for item in data if item['is_answered'])
        unanswered = len(data) - answered
        result = {"answered": answered, "unanswered": unanswered}
        print("Endpoint `/answered-status`:", result)  # Imprimir en consola
        return jsonify(result)

# 2. Obtener la respuesta con mayor reputación
@api.route('/highest-reputation')
class HighestReputation(Resource):
    def get(self):
        """
        Obtener la respuesta con mayor reputación
        """
        data = fetch_data()
        highest = max(data, key=lambda x: x['owner']['reputation'])
        result = {"highest_reputation": highest}
        print("Endpoint `/highest-reputation`:", result)  # Imprimir en consola
        return jsonify(result)

# 3. Obtener la respuesta con menor número de vistas
@api.route('/lowest-views')
class LowestViews(Resource):
    def get(self):
        """
        Obtener la respuesta con menor número de vistas
        """
        data = fetch_data()
        lowest = min(data, key=lambda x: x['view_count'])
        result = {"lowest_views": lowest}
        print("Endpoint `/lowest-views`:", result)  # Imprimir en consola
        return jsonify(result)

# 4. Obtener la respuesta más vieja y más actual
@api.route('/oldest-newest')
class OldestNewest(Resource):
    def get(self):
        """
        Obtener la respuesta más vieja y más reciente
        """
        data = fetch_data()
        oldest = min(data, key=lambda x: x['creation_date'])
        newest = max(data, key=lambda x: x['creation_date'])
        result = {"oldest": oldest, "newest": newest}
        print("Endpoint `/oldest-newest`:", result)  # Imprimir en consola
        return jsonify(result)

# 5. Obtener la respuesta con menor número de vistas (punto adicional)
@api.route('/least-viewed')
class LeastViewed(Resource):
    def get(self):
        """
        Obtener la respuesta con menor número de vistas (agregado como punto faltante)
        """
        data = fetch_data()
        least_viewed = min(data, key=lambda x: x['view_count'])
        result = {"least_viewed": least_viewed}
        print("Endpoint `/least-viewed`:", result)  # Imprimir en consola
        return jsonify(result)
