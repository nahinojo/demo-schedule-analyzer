import os
from datetime import date

from flask import Flask
from flask_cors import CORS

from .config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
environment = os.environ.get('FLASK_ENV', 'development')
configuration = configurations[environment]
app.config.from_object(configuration)
CORS(app)

PATH_TO_TEMP = os.path.dirname(os.path.realpath(__file__)) + '/temp'
PATH_TO_CALENDAR = PATH_TO_TEMP + '/demo-calendar.ics'
PATH_TO_SCHEDULE = PATH_TO_TEMP + '/demo-schedule.xlsx'
CURRENT_YEAR = date.today().year
