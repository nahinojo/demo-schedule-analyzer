from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Session = sessionmaker(engine)
Base.metadata.create_all(engine)

from app.database.setup_db import setup_db
