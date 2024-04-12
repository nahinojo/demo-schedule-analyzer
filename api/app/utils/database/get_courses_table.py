from app.database import Session
from app.models import Course
from sqlalchemy import select


def get_courses_table():
    """
    Retrieves all courses from the database as a dictionary.

    Returns
    -------
    courses_table: dict
        The dictionary of all courses.
    """
    with Session() as session:
        stmt = select(Course)
        courses = session.execute(stmt).scalars().all()
        courses_table = {
            course.id: {
                "courseCode": course.course_code,
                "instructor": course.instructor,
                "term": course.term,
                "year": course.year,
                "numDemoEvents": len(course.demo_events)
            } for course in courses
        }
    return courses_table
