from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from section1 import section1_blueprint

def create_app():
    """
    Crea y configura la aplicación Flask.
    """
    app = Flask(__name__)

    # Configurar CORS
    CORS(app)

    # Configuración de Swagger para el proyecto completo
    api = Api(app, version='1.0', title='Backend Project', description='Documentación de la API para el proyecto Backend, que incluye múltiples secciones.', doc='/swagger')

    # Registrar el blueprint para el Ejercicio 1 (sección 1)
    app.register_blueprint(section1_blueprint, url_prefix="/api/section1")

    # Puedes registrar las otras secciones si las tienes
    # app.register_blueprint(section2_blueprint, url_prefix="/api/section2")
    # app.register_blueprint(section3_blueprint, url_prefix="/api/section3")

    return app


if __name__ == '__main__':
    # Correr la app solo si este es el archivo principal
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8087)
