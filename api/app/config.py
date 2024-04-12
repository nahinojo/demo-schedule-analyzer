import os


class Config:
    DEBUG = False
    TESTING = False
    # DATABASE_PATH differs depending on running in Docker vs CLI.
    SQLALCHEMY_DATABASE_PATH = f"{os.getcwd()}/app/database/main.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{SQLALCHEMY_DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
