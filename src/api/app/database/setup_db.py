from app.database import Session
from app.utils import extract_courses_from_calendar


def setup_db():
    """
    Initializes the database with data from the demo calendar.
    """
    with Session() as session:
        all_courses = extract_courses_from_calendar()
        for course in all_courses:
            session.add(course)
        session.commit()
    return
