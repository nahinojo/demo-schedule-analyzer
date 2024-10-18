"""
Tests the following:
    - Creation of the Schedule model.
    - Adding a Schedule to the database.
"""
from flask import Flask
from sqlalchemy.orm import Session

from app.daos import ScheduleDAO
from app.models import Schedule


def create_schedule_test(app: Flask,
                         schedule: Schedule
                         ) -> None:
    """
    Tests the creation of the Schedule model, and associated child models.
    """
    assert schedule.course_id == 1
    assert schedule.schedule_data is not None


def add_schedule_to_db_test(db_session: Session,
                            schedule: Schedule
                            ) -> None:
    """
    Tests the addition of the Schedule to the database.
    """
    with db_session.begin():
        prior_count = ScheduleDAO.get_count(session=db_session)
        ScheduleDAO.add(session=db_session, schedule=schedule)
        post_count = ScheduleDAO.get_count(session=db_session)
        assert post_count == prior_count + 1
        db_session.rollback()
