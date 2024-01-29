from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(engine)