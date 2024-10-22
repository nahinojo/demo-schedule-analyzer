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

    @classmethod
    def _get_model_type(cls) -> ModelType:
        """
        The model class for this DAO.
        """
        return cls._model_type

    @classmethod
    def get_by_id(cls,
                  session: Session,
                  model_id: int
                  ) -> ModelType | None:
        """
        Retrieves a model from the database.

        Parameters
        ----------
        session: Session
            The database session.
        model_id: int
            The ID of the course to retrieve.

        Returns
        -------
        ModelType
            The retrieved model, or None if not found.
        """
        model_type = cls._get_model_type()
        return session.execute(
            select(model_type).where(model_type.id == model_id)
            ).scalar_one_or_none()

    @classmethod
    def get_all(cls, 
                session: Session,
                ) -> list[ModelType]:
        """
        Retrieves all models from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        List[ModelType]
            The list of retrieved models.
        """
        model_type = cls._get_model_type()
        return session.execute(select(model_type)).scalars().all()

    @classmethod
    def get_count(cls,
                  session: Session,
                  ) -> int:
        """
        Retrieves the count of all models from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        int
            The count of retrieved models.
        """
        return len(cls.get_all(session))

    @classmethod
    def add(cls,
            session: Session,
            model: ModelType
            ) -> None:
        """
        Adds a model to the database.

        Parameters
        ----------
        session: Session
            The database session.
        model: ModelType
            The model to add to the database.
        """
        session.add(model)
        return
