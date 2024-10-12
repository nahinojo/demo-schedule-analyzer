"""
Configuration for the production environment.
"""
from .config import Config


class ProductionConfig(Config):
    """
    Configuration for the production environment.
    """
    def __init__(self):
        super().__init__()
        self.debug = False
        self.sqlalchemy_track_modifications = False
