# backend/__init__.py
from flask import Flask
from flask_cors import CORS # Importar Flask-CORS

def create_app():
    app = Flask(__name__)
    CORS(app) # Habilitar CORS para permitir peticiones desde el frontend Astro

    # Puedes añadir configuraciones aquí
    # app.config.from_object('backend.config.Config') # Si usas un archivo de config

    # Registrar Blueprints
    from .routes import programacion_routes
    app.register_blueprint(programacion_routes.bp)

    return app