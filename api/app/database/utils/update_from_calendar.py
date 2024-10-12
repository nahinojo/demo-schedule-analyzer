"""
Utility function for clearing the database.
"""
from flask import Flask

from . import session_scope
from . import clear_all
from app.models import Base
from app.utils.calendar import extract_courses_from_calendar


def update_from_calendar(app: Flask):
    """
    Updates the database with current demo calendar data.
    """
    clear_all()
    with session_scope() as session:
        all_courses = extract_courses_from_calendar(app)
        for course in all_courses:
            session.add(course)
