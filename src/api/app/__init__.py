import os
from flask import Flask
from flask_cors import CORS

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

PATH_TO_TEMP = os.path.dirname(os.path.realpath(__file__)) + '/temp'
PATH_TO_CALENDAR = PATH_TO_TEMP + '/demo-calendar.ics'
PATH_TO_SCHEDULE = PATH_TO_TEMP + '/demo-schedule.xlsx'
