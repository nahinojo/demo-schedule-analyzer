"""
Tests the config module.

"""
from sqlalchemy.testing.plugin.plugin_base import config


def config_test():
    """
    Asserts Config is a singleton.
    """
    from app.config import Config
    from app.config import ConfigManager

    ConfigManager.set_config()
    config1 = ConfigManager.get_config()

    assert config1.current_year == 2024
