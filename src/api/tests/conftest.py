from create_app import create_app

import pytest


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def app_context(app):
    with app.app_context():
        yield
