import pytest


@pytest.fixture()
def app():
    from app import app
    app.config.from_object('app.config.TestingConfig')
    yield app
    return


@pytest.fixture()
def app_context(app):
    with app.app_context():
        yield
    return
