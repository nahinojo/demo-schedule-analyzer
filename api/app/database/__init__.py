"""
The database module.
"""
import os

from sqlalchemy import create_engine
from flask import Flask

from app.models import Base
from .database import Database


def init_db(app: Flask) -> None:
    """
    Initializes the database.

    Parameters
    ----------
    app: Flask
        The Flask application.

    Returns
    -------
    None
    """
    db_path = app.config["DATABASE_PATH"]
    if os.path.isfile(db_path):
        os.remove(db_path)
    with open(db_path, "w+") as f:
        f.write("")
    engine = create_engine(app.config["DATABASE_URI"])
    Base.metadata.create_all(engine)
    Database.init(engine)
