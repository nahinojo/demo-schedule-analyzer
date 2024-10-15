"""
The database module.
"""
import os

from flask import current_app
from app.models import Base

from .database import Database


def init_db() -> None:
    """
    Initializes the database.

    Returns
    -------
    None
    """
    if current_app.config["APP_ENV"] != "testing":
        db_path = current_app.config["DATABASE_PATH"]
        if os.path.isfile(db_path):
            os.remove(db_path)
        with open(db_path, "w+") as f:
            f.write("")
    Database.init()
    Base.metadata.create_all(Database.get_engine())
