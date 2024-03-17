from datetime import date
from sqlalchemy import select

from app.database import Session
from app.models import Course


def get_course_table():
    with Session() as session:
        stmt = select(Course)
        courses = session.execute(stmt).scalars().all()
        print(courses)
        course_table = {
            course.id: {
                "course_code": course.course_code,
                "instructor": course.instructor,
                "term": course.term,
                "year": course.year,
                "number_of_demo_events": len(course.demo_events)
            } for course in courses
        }
    return course_table
