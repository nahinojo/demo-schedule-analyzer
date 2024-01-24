# from create_app import create_app
import pytest


@pytest.fixture()
def test_request_example(client):
    response = client.get("/posts")
    assert b"<h2>Hello, World!</h2>" in response.data


# # See https://flask.palletsprojects.com/en/3.0.x/testing/ and modify later.
# if __name__ == '__main__':
#     app = create_app()
#     app.testing = True
#     app.test_client()
