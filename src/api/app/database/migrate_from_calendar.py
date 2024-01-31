from app.database import Session
from app.utils import extract_course_details_from_calendar


def migrate_from_calendar():
    """
    Initializes the database with data from the demo calendar.
    """
    with Session() as session:
        all_courses = extract_course_details_from_calendar()
        for course in all_courses:
            session.add(course)
        session.commit()
    return
