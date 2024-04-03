import os


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_PATH = f"{os.getcwd()}/src/api/app/database/main.db"
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
