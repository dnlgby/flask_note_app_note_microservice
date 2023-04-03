# Copyright (c) 2023 Daniel Gabay

import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from app.di.service_module import ServiceModule
from app.resources import NoteBlueprint


def create_app():
    app = Flask(__name__)

    # Cross-Origin Resource Sharing
    CORS(app)

    # Load environment variables from existing '.env' files
    load_dotenv()

    # Flask
    app.config["PROPOGATE_EXCEPTION"] = True

    # API info
    app.config["API_TITLE"] = "Note service REST API"
    app.config["API_VERSION"] = "v1"

    # Open API
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Flask-smorest documentation
    api = Api(app)
    api.register_blueprint(NoteBlueprint)

    # JWT - Will set on code for now for developing purposes
    secret_key = os.getenv('JWT_SECRET_KEY')
    if secret_key is None:
        raise ValueError("The JWT_SECRET_KEY environment variable must be set")

    app.config['JWT_SECRET_KEY'] = secret_key
    jwt = JWTManager(app)

    # Dependency injection
    FlaskInjector(app=app, modules=[ServiceModule])

    return app
