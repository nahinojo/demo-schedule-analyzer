import os


class Config:
    DEBUG = False
    TESTING = False
    """
    For some reason, the api calls can't access the database.
    
    Online suggestions mention this is due to using an in-memory database. As a solution, I am setting up a database 
    to use. It's not fully setup and needs some tinkering.
    
    Continue from here.
    """
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{os.getcwd()}/src/api/app/database/foo.db"
    print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
