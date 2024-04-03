from datetime import date

from app.database import Session
from app.models import Course
from sqlalchemy import select


def get_courses():
    """
    Retrieves the list of all courses from the database.

    Returns
    -------
    course_table: dict
        The dictionary of all courses.
    """
    with Session() as session:
        stmt = select(Course)
        courses = session.execute(stmt).scalars().all()
        course_table = {
            course.id: {
                "courseCode": course.course_code,
                "instructor": course.instructor,
                "term": course.term,
                "year": course.year,
                "numDemoEvents": len(course.demo_events)
            } for course in courses
        }
    return course_table
