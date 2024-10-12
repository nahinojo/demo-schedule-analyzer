"""
Tests the config module.

"""

from _pytest.monkeypatch import MonkeyPatch


def config_test(monkeypatch: MonkeyPatch):
    """
    Asserts Config is a singleton.
    """
    from datetime import date
    monkeypatch.setenv("APP_ENV", "testing")

    from app import create_app
    app = create_app()
    assert app.config["CURRENT_YEAR"] == date.today().year
    assert app.config["TESTING"] is True
