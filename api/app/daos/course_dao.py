"""
Course Data Access Object (DAO).
"""
from sqlalchemy.orm import Session
from app.models import Course
from ._base_dao import _BaseDAO


class CourseDAO(_BaseDAO):
    """
    Course Data Access Object (DAO).
    """

    @staticmethod
    def get_by_id(session: Session,
                  course_id: int,
                  **kwargs) -> Course | None:
        """
        Retrieves a course from the database.

        Parameters
        ----------
        session: Session
            The database session.
        course_id: int
            The ID of the course to retrieve.

        Returns
        -------
        Course
            The retrieved course, or None if not found.
        """
        return _BaseDAO.get_by_id(session, Course, course_id)

    @staticmethod
    def get_all(session: Session,
                **kwargs
                ) -> list[Course]:
        """
        Retrieves a course from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        Course
            The retrieved course, or None if not found.
        """
        return _BaseDAO.get_all(session, Course)

    @staticmethod
    def add(session: Session,
            course: Course
            ) -> None:
        """
        Adds a course to the database.

        Parameters
        ----------
        session: Session
            The database session.
        course: Course
            The course to add.
        """
        session.add(course)
