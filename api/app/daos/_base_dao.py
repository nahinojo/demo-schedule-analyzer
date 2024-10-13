"""
Base Data Access Object (DAO).
"""
from sqlalchemy.orm import Session
from app.types import ModelType
from sqlalchemy import select


class _BaseDAO:
    """
    Base Data Access Object (DAO). Should not be used directly, only
    inherited.
    """

    @staticmethod
    def get_by_id(session: Session,
                  model: ModelType,
                  model_id: int
                  ) -> ModelType | None:
        """
        Retrieves a model from the database.

        Parameters
        ----------
        session: Session
            The database session.
        model: ModelType
            The model class to retrieve.
        model_id: int
            The ID of the course to retrieve.

        Returns
        -------
        ModelType
            The retrieved model, or None if not found.
        """
        return session.execute(
            select(model).where(model.id == model_id)
        ).scalar_one_or_none()

    @staticmethod
    def get_all(session: Session,
                model: ModelType
                ) -> list[ModelType]:
        """
        Retrieves all models from the database.

        Parameters
        ----------
        session: Session
            The database session.
        model: ModelType
            The model class to retrieve.

        Returns
        -------
        List[ModelType]
            The list of retrieved models.
        """
        return session.execute(select(ModelType)).scalars().all()

    @staticmethod
    def add(session: Session,
            model: ModelType
            ) -> None:
        """
        Adds a model to the database.

        Parameters
        ----------
        session: Session
            The database session.
        model: ModelType
            The model to add.
        """
        session.add(model)
