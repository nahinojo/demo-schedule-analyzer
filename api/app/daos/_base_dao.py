"""
Base Data Access Object (DAO).
"""
from abc import ABC
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.types import ModelType


class _BaseDAO(ABC):
    """
    Base Data Access Object (DAO).
    """
    _model_type = None
    _session = None

    def __init__(self,
                 session: Session
                 ) -> None:
        """
        Initializes the DAO.

        Parameters
        ----------
        session: Session
            The database session.
        """
        self._session = session

    @property
    def session(self) -> Session:
        """
        The database session.
        """
        return self._session

    @property
    def model_type(self) -> ModelType:
        """
        The model class for this DAO. Changes with each subclass.
        """
        return self._model_type

    def get_by_id(self,
                  model_id: int
                  ) -> ModelType | None:
        """
        Retrieves a model from the database.

        Parameters
        ----------
        model_id: int
            The ID of the course to retrieve.

        Returns
        -------
        ModelType
            The retrieved model, or None if not found.
        """
        model_type = self.model_type
        return self.session.execute(
            select(model_type).where(model_type.id == model_id)
        ).scalar_one_or_none()

    def get_all(self) -> list[ModelType]:
        """
        Retrieves all models from the database.

        Returns
        -------
        List[ModelType]
            The list of retrieved models.
        """
        model_type = self.model_type
        return self.session.execute(select(model_type)).scalars().all()

    def get_count(self) -> int:
        """
        Retrieves the count of all models from the database.

        Returns
        -------
        int
            The count of retrieved models.
        """
        return len(self.get_all())

    def add(self,
            model: ModelType
            ) -> None:
        """
        Adds a model to the database.

        Parameters
        ----------
        model: ModelType
            The model to add to the database.
        """
        self.session.add(model)
        return
