"""
Course Data Access Object (DAO).
"""
from app.database import Database
from app.models import Course
from sqlalchemy import select


class CourseDAO:
    """
    Course Data Access Object (DAO).
    """

    @staticmethod
    def get_course_by_id(course_id):
        """
        Retrieves a course from the database.

        Parameters
        ----------
        course_id: int
            The ID of the course to retrieve.

        Returns
        -------
        Course
            The retrieved course, or None if not found.
        """
        session = Database.get_session()
        return session.execute(
            select(Course).where(Course.id == course_id)
        ).scalar_one_or_none()

    def get_all(self):
        """
        Retrieves all courses from the database.

        Returns
        -------
        courses: List[Course]
            The list of retrieved courses.
        """
        return self.session.execute(
            select(Course)
        ).scalars().all()

    def create(course: Course) -> Course:
        """
        Creates a course in the database.

        Parameters
        ----------
        course: Course
            The course to create.

        Returns
        -------
        Course
            The created course.
        """
        with Database.Session() as session:
            session.add(course)
            session.commit()
        return course
