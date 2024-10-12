"""
Fills the database with current demo calendar data.
"""
from app.database import Session
from app.utils import extract_courses_from_calendar
from app.database.clear_db import clear_db


def fill_db_from_calendar():
    """
    Adds all courses from the calendar to the database.

    Returns
    -------
    None
    """
    clear_db()
    with Session() as session:
        all_courses = extract_courses_from_calendar()
        for course in all_courses:
            session.add(course)
        session.commit()
    return
