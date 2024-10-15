"""
Utility function for clearing the database.
"""
from . import session_scope
from . import empty_db
from app.utils.calendar import extract_courses_from_calendar


def update_db_from_calendar():
    """
    Updates the database with current demo calendar data.
    """
    empty_db()
    with session_scope() as session:
        all_courses = extract_courses_from_calendar()
        for course in all_courses:
            session.add(course)
