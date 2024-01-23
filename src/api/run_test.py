from create_app import create_app
import pytest

# See https://flask.palletsprojects.com/en/3.0.x/testing/ and modify later.
if __name__ == '__main__':
    app = create_app()
    app.testing = True
    app.test_client()
