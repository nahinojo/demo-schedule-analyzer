"""
Initializes the API.
"""
import os
from flask import Flask
from flask_cors import CORS

from app.config import (
    Config,
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)

from app.database import Database
from app.lifecycle import register_lifecycle_hooks


def create_app():
    """
    Creates the Flask app.
    """
    app = Flask(__name__)
    app_env = os.environ.get('APP_ENV', 'development')
    configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    app.config.from_object(configs[app_env])
    app.config["APP_ENV"] = app_env
    with app.app_context():
        register_lifecycle_hooks()
        Database.init()
        CORS(app)
    return app
