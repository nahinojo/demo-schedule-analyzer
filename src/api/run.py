import sqlalchemy

from app import app
from app.database import Session
from app.database.setup_db import setup_db
from app.models import Course
from app.routes import api_blueprint


setup_db()
app.register_blueprint(api_blueprint, url_prefix='/api')
app.run()
