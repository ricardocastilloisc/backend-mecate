import os
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from section1 import section1_blueprint
from section2 import section2_blueprint
from models.models import db
from insertar_datos import insertar_datos

def create_app():
    """
    Crea y configura la aplicación Flask.
    """
    app = Flask(__name__)

    # Configurar CORS
    CORS(app)

    # Definir carpeta para la base de datos
    db_folder = os.path.join(os.getcwd(), "data")
    db_path = os.path.join(db_folder, "vuelos.db")

    # Crear carpeta si no existe
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Configurar base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar SQLAlchemy
    db.init_app(app)

    # Configuración de Swagger para el proyecto completo
    api = Api(
        app, 
        version='1.0', 
        title='Backend Project', 
        description='Documentación de la API para el proyecto Backend, que incluye múltiples secciones.', 
        doc='/swagger'
    )

    # Crear base de datos y tablas si no existen
    if not os.path.exists(db_path):
        with app.app_context():
            print("Base de datos no encontrada. Creando tablas...")
            db.create_all()
            print("Tablas creadas con éxito.")
            insertar_datos()
            print("Datos creados con éxito.")

    # Registrar el blueprint para el Ejercicio 1 (sección 1)
    app.register_blueprint(section1_blueprint, url_prefix="/api/section1")
    app.register_blueprint(section2_blueprint, url_prefix="/api/section2")

    return app


if __name__ == '__main__':
    # Correr la app solo si este es el archivo principal
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8087)
