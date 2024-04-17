import os


class Config:
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
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
