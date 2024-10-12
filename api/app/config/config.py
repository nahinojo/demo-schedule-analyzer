"""
Abstract base class for configuration. Config should not be used directly as
the final configuration. Meant to be inherited by environment-specific
configurations (e.g., DevelopmentConfig, TestingConfig).

Notice how it cannot have any app dependencies.
"""
import os
from datetime import date


class Config:
    """
    Configuration for the application.
    """
    __instance = None
    __isInitialized = False

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("Creating Config instance")
            cls.__instance = super(Config, cls).__new__(cls)
            print("Config instance created")
        return cls.__instance

    def __init__(self):
        """
        Configuration for the Flask app. Paths are specified relative to the
        current working directory.
        """

        if not self.__isInitialized:
            print("Initializing Config instance")
            self.testing = False
            self.current_year = date.today().year

            # Database path differs between docker container and local
            cwd = os.getcwd()
            self.cwd = cwd
            if "api" not in cwd[-4:]:
                if cwd[-1] == "/":
                    self.db_path = \
                        f"{cwd}api/app/database/main.db"
                else:
                    self.db_path = \
                        f"{cwd}/api/app/database/main.db"
            else:
                self.db_path = f"{cwd}/app/database/main.db"
            self.db_uri = f"sqlite:////{self.db_path}"
            self.temp_path = \
                f"{cwd}/temp"  # Let's see if simplifying this works...
            # f"{os.path.dirname(os.path.realpath(__file__))}/temp"
            self.calendar_path = f"{self.temp_path}/demo-calendar.ics"
            self.schedule_xlsx_path = f"{self.temp_path}/demo-schedule.xlsx"

            self.__isInitialized = True
            print("Config instance initialized")
