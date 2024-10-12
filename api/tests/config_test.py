"""
Tests the config module.

"""

from _pytest.monkeypatch import MonkeyPatch


def testing_config_test(monkeypatch: MonkeyPatch):
    """
    Ensures testing config can be set.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    from app import create_app
    app = create_app()
    assert app.config["APP_ENV"] == "testing"


def production_config_test(monkeypatch: MonkeyPatch):
    """
    Ensures production config can be set.
    """
    monkeypatch.setenv("APP_ENV", "production")
    from app import create_app
    app = create_app()
    assert app.config["APP_ENV"] == "production"


def development_config_test(monkeypatch: MonkeyPatch):
    """
    Ensures development config can be set.
    """
    monkeypatch.setenv("APP_ENV", "development")
    from app import create_app
    app = create_app()
    assert app.config["APP_ENV"] == "development"
