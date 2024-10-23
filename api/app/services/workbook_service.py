"""
Handles workbook data operations.
"""

from sqlalchemy.orm import Session


class WorkbookService:
    """
    Handles workbook data operations.
    """

    def __init__(self,
                 session: Session,
                 course_id: int
                 ):
        """
        Initializes the WorkbookService class.

        Parameters
        ----------
        session: Session
            The database session.
        course_id: int
            The ID of the course to construct the workbook for.
        """
        self._session = session
        self._course_id = course_id
        self._workbook = self._create_workbook()