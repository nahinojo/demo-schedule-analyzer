"""
Fixtures for testing.
"""
import pytest


@pytest.fixture()
def app(monkeypatch: pytest.MonkeyPatch):
    """
    Fixture to create Flask app based on the current environment.
    """
    from flask import Flask
    from app import create_app

    def _app(env: str = "testing") -> Flask:
        monkeypatch.setenv("APP_ENV", env)
        return create_app()

    yield _app

    from app.database import Database
    Database.end()
