from models import Demo, DemoEvent, db
from utils.database import add_course, add_demo, add_demo_event


def add_and_edit_course():
    print("Executing routes.add_and_edit_course()...")
    course_id = add_course(
        course_code="7C",
        instructor="Krivorotov",
        term="Fall",
        year=2022,
        demo_event=[]
    )

