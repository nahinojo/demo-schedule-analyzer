from app.database import Session
from app.utils import request_calendar


def migrate():
    request_calendar()
    with Session() as session:
        pass
