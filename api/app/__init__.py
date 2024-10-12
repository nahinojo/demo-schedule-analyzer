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

from app.database import init_db


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
    init_db(app)
    CORS(app)

    return app
