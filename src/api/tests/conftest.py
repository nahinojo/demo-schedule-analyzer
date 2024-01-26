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


# @pytest.fixture()
# def test_course():
#     return ModelFactory.create_course()
#
#
# @pytest.fixture()
# def test_demo_event(test_course):
#     return test_course.demo_events[0]
