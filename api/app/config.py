"""
Configuration for the Flask app.
"""

import os


class Config:
    """
    Configuration for the Flask app.
    """
    TESTING = False
    # Database path differs between docker container and local development
    CWD = os.getcwd()
    if "api" not in CWD[-4:]:
        if CWD[-1] == "/":
            SQLALCHEMY_DATABASE_PATH = f"{CWD}api/app/database/main.db"
        else:
            SQLALCHEMY_DATABASE_PATH = f"{CWD}/api/app/database/main.db"
    else:
        SQLALCHEMY_DATABASE_PATH = f"{CWD}/app/database/main.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{SQLALCHEMY_DATABASE_PATH}"


class DevelopmentConfig(Config):
    """
    Configuration for the development environment.
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Configuration for the production environment.
    """
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Configuration for the testing environment.
    """
    TESTING = True
