"""
Configuration for the Pytest testing environment.
"""

from .config import Config


class TestingConfig(Config):
    """
    Configuration for the testing environment.
    """
    def __init__(self):
        super().__init__()
        self.testing = True
        self.sqlalchemy_database_uri = 'sqlite:///:memory:'
