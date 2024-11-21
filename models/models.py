
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

# Definición de las tablas

class Aerolinea(db.Model):
    __tablename__ = 'aerolineas'
    id_aerolinea = db.Column(db.Integer, primary_key=True)
    nombre_aerolinea = db.Column(db.String(100), nullable=False)

class Aeropuerto(db.Model):
    __tablename__ = 'aeropuertos'
    id_aeropuerto = db.Column(db.Integer, primary_key=True)
    nombre_aeropuerto = db.Column(db.String(100), nullable=False)

class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id_movimiento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

class Vuelo(db.Model):
    __tablename__ = 'vuelos'
    id_vuelo = db.Column(db.Integer, primary_key=True)
    id_aerolinea = db.Column(db.Integer, db.ForeignKey('aerolineas.id_aerolinea'), nullable=False)
    id_aeropuerto = db.Column(db.Integer, db.ForeignKey('aeropuertos.id_aeropuerto'), nullable=False)
    id_movimiento = db.Column(db.Integer, db.ForeignKey('movimientos.id_movimiento'), nullable=False)
    dia = db.Column(db.Date, nullable=False)

    # Relaciones
    aerolinea = db.relationship('Aerolinea', backref='vuelos')
    aeropuerto = db.relationship('Aeropuerto', backref='vuelos')
    movimiento = db.relationship('Movimiento', backref='vuelos')

