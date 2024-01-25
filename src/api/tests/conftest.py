from create_app import create_app
from database import db
from tests.utils.model_factory import ModelFactory

import pytest


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
    return


@pytest.fixture()
def app_context(app):
    with app.app_context():
        yield
    return


@pytest.fixture()
def test_course():
    return ModelFactory.create_course()


@pytest.fixture()
def test_demo_event(test_course):
    return test_course.demo_events[0]


@pytest.fixture()
def app_context_with_test_course(app_context, test_course):
    db.session.add(test_course)
    db.session.commit()
    yield
    db.session.delete(test_course)
    return
