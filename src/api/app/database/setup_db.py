from app.database import Session
from app.models import Base
from app.utils import extract_courses_from_calendar


def setup_db():
    """
    Initializes the database with data from the demo calendar.
    """
    with Session() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        all_courses = extract_courses_from_calendar(
            target_year= 2018
        )
        for course in all_courses:
            session.add(course)
        session.commit()
    return
