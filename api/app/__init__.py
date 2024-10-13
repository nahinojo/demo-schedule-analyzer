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

from app.database import init_db, Database
from app.lifecycle import register_lifecycle_hooks
from app.database.utils import update_db_from_calendar


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
    init_db(app)
    register_lifecycle_hooks(app)
    CORS(app)

    if app_env != 'testing':
        update_db_from_calendar(app)
    return app
