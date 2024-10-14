"""
Testing for demo model.
"""
from flask import Flask
from sqlalchemy.orm import Session
from app.models import Demo
from app.daos import DemoDAO


def create_demo_test(app: Flask, demo: Demo) -> None:
    """
    Tests the creation of the demo model.
    """
    with app.app_context():
        assert demo.name == "DEMO_TEST"


def add_demo_to_db_test(db_session: Session, demo: Demo) -> None:
    """
    Tests the adding of a demo to the database.
    """
    with db_session.begin():
        count = DemoDAO.get_count(db_session)
        DemoDAO.add(db_session, demo)
        assert count == DemoDAO.get_count(db_session) - 1
