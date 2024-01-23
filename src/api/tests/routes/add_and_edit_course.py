from database import db
from models import Demo, DemoEvent
from utils.database import create_course, create_demo, create_demo_event


def add_and_edit_course():
    print("Executing routes.add_and_edit_course()...")
    course_id = create_course(
        course_code="7C",
        instructor="Krivorotov",
        term="Fall",
        year=2022,
        demo_event=[]
    )

