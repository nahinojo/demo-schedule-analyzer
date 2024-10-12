"""
Configuration for the development environment.

"""
from .config import Config


class DevelopmentConfig(Config):
    """
    Configuration for the development environment.
    """
    def __init__(self):
        super().__init__()
        self.debug = True
        self.sqlalchemy_track_modifications = True
