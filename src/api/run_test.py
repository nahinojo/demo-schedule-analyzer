from create_app import create_app
import pytest


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
