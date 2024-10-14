"""
Testing for DemoEvent model.
"""
from datetime import datetime
from flask import Flask
from sqlalchemy.orm import Session

from app.models import Demo, DemoEvent
from app.daos import DemoEventDAO


def demo_event_test(app: Flask,
                    demo: Demo,
                    demo_event: DemoEvent
                    ) -> None:
    """
    Tests the creation of the demo event model.
    """
    with app.app_context():
        assert demo_event.event_date == datetime.now().date()
        assert demo_event.additional_information == (
            "ADDITIONAL_INFORMATION_TEST"
        )
        assert demo_event.demos == [demo]


def add_demo_event_to_db_test(db_session: Session,
                              demo_event: DemoEvent) -> None:
    """
    Tests the addition of a demo event to the database.
    """
    with db_session.begin():
        count = DemoEventDAO.get_count(db_session)
        DemoEventDAO.add(db_session, demo_event)
        assert count == DemoEventDAO.get_count(db_session) - 1
