"""
Configuration manager.

"""
import os

from .config import Config
from .development_config import DevelopmentConfig
from .testing_config import TestingConfig
from .production_config import ProductionConfig


# Global configuration accessor
class ConfigManager:
    """
    Configuration manager.
    """
    _config = None

    @classmethod
    def set_config(cls):
        """
        Sets the configuration for the given environment.
        """

        configs = {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
            'production': ProductionConfig
        }
        env = os.environ.get('APP_ENV', 'development')
        print("Setting config for environment: " + env)
        print("configs:", configs)
        print("env:", env)
        print("configs[env]:", configs[env])
        cls._config = configs[env]()

    @classmethod
    def get_config(cls) -> Config:
        """
        Returns the configuration.
        """
        if cls._config is None:
            raise ValueError(
                "Configuration has not been set. Call set_config() first.")
        return cls._config
