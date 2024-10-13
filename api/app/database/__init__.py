"""
The database module.
"""
import os

from flask import Flask

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
    if app.config["APP_ENV"] != "testing":
        db_path = app.config["DATABASE_PATH"]
        if os.path.isfile(db_path):
            os.remove(db_path)
        with open(db_path, "w+") as f:
            f.write("")
    from app.models import Base
    Database.init(db_uri=app.config["DATABASE_URI"])
    Base.metadata.create_all(Database.get_engine())
