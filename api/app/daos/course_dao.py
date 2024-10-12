"""
Course Data Access Object (DAO).
"""
from app.database import Session
from app.models import Course
from sqlalchemy import select


class CourseDAO:
    """
    Course Data Access Object (DAO).
    """
    def __init__(self, session: Session):
        """
        Initializes the DAO.

        Parameters
        ----------
        session: Session
            The session to use for database operations.
        """
        self.session = session

    def get(self, course_id):
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
        return self.session.execute(
            select(Course).where(Course.id == course_id)
        ).scalar_one_or_none()
