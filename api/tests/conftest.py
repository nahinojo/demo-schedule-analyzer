"""
Fixtures for testing.
"""
import pytest
from flask import Flask
from app import create_app


@pytest.fixture()
def app(monkeypatch: pytest.MonkeyPatch) -> Flask:
    """
    Fixture to create Flask app based on the current environment.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    app = create_app()
    yield app
