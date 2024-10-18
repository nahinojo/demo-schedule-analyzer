"""
Abstract base class for configuration. Config should not be used directly as
the final configuration. Meant to be inherited by environment-specific
configurations (e.g., DevelopmentConfig, TestingConfig).

Notice how it cannot have any app dependencies.
"""
import os


class Config:
    """
    Configuration for the application.
    """
    TESTING = False

    # Database path differs between docker container and local
    CWD = os.getcwd()
    CWD = CWD
    if "api" not in CWD[-4:]:
        if CWD[-1] == "/":
            DATABASE_PATH = \
                f"{CWD}api/app/database/main.db"
        else:
            DATABASE_PATH = \
                f"{CWD}/api/app/database/main.db"
    else:
        DATABASE_PATH = f"{CWD}/app/database/main.db"
    DATABASE_URI = f"sqlite:////{DATABASE_PATH}"
    TEMP_PATH = f"{CWD}/app/temp"
    CALENDAR_PATH = f"{TEMP_PATH}/demo-calendar.ics"
    SCHEDULE_XLSX_PATH = f"{TEMP_PATH}/demo-schedule.xlsx"
    IS_DATABASE_EMPTY = False


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
    DATABASE_URI = 'sqlite:///:memory:'
    IS_DATABASE_EMPTY = True  # Empty for most test cases, but not all.
