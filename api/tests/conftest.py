"""
Fixtures for testing.
"""
import pytest
from flask import Flask
from sqlalchemy.orm import Session

from app import create_app
from app.database import Database
from app.models import Course, Demo, DemoEvent
from tests.utils import random_course, random_demo_event, random_demo


# App
@pytest.fixture()
def app(monkeypatch: pytest.MonkeyPatch) -> Flask:
    """
    Flask app fixture for testing.

    Parameters
    ----------
    monkeypatch: pytest.MonkeyPatch
        The monkeypatch fixture for configuring the environment.

    Returns
    -------
    Flask
        The generated Flask app.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    app = create_app()
    yield app


# Database
@pytest.fixture
def db_session(app: Flask) -> Session:
    """
    Database session.

    Parameters
    ----------
    app: Flask
        The Flask app fixture.

    Returns
    -------
    Session
        The database session.
    """
    with app.app_context():
        _session = Database.get_session()
        yield _session
        _session.close()


# Models
@pytest.fixture()
def demo() -> Demo:
    """
    Demo fixture that can be used in testing.

    Returns
    -------
    Demo
        The generated demo.
    """
    yield random_demo()


@pytest.fixture
def demo_event(demo) -> DemoEvent:
    """
    DemoEvent fixture that can be used in testing.

    Parameters
    ----------
    demo: Demo
        The demo fixture to be associated with the demo event.

    Returns
    -------
    DemoEvent
        The generated demo event.
    """
    yield random_demo_event(demos=[demo])


@pytest.fixture
def course(demo_event) -> Course:
    """
    Course fixture that can be used in testing.

    Parameters
    ----------
    demo_event: DemoEvent
        The demo_event fixture to be associated with the course.

    Returns
    -------
    Course
        The generated course.
    """
    yield random_course(demo_events=[demo_event])
