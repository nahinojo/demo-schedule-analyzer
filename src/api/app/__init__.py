from app.config import *

from flask import Flask
from flask_cors import CORS


def create_app(configuration=Config):
    app = Flask(__name__)
    app.config.from_object(configuration)
    return app
