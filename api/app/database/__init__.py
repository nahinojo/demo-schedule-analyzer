import os

from app import app
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_path = app.config["SQLALCHEMY_DATABASE_PATH"]
if os.path.isfile(database_path):
    os.remove(database_path)
with open(database_path, "w+") as f:
    f.write("")

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Session = sessionmaker(engine)
Base.metadata.create_all(engine)
