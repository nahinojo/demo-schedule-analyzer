from datetime import date
from sqlalchemy import select

from app.database import Session
from app.models import Course


def get_filtered_courses(
        target_course_code: str = None,
        target_instructor: str = None,
        target_term: str = None,
        target_year: int = date.today().year,
        is_target_year_as_minimum: bool = True,
):
    """
    Retrieves the union set of all courses where the provided attributes match. Each course is expected to match all the
    provided attributes.

    Parameters
    ----------
    target_course_code: str
        The target course code.
    target_instructor: str
        The target instructor.
    target_term: str
        The target term.
    target_year: int
        The target year.
    is_target_year_as_minimum: bool
        Whether the target year is the minimum year.

    Returns
    -------
    list[Course]
        A list of Course objects.
    """
    with Session() as session:
        stmt = select(Course)
        if target_course_code:
            stmt = stmt.filter(Course.course_code == target_course_code)
        if target_instructor:
            stmt = stmt.filter(Course.instructor == target_instructor)
        if target_term:
            stmt = stmt.filter(Course.term == target_term)
        if is_target_year_as_minimum:
            stmt = stmt.filter(Course.year >= target_year)
        else:
            stmt = stmt.filter(Course.year == target_year)
        courses = session.execute(stmt).scalars().all()
    return courses
