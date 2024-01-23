from database import db
from models import Demo, DemoEvent


def create_demo(
        name: str,
        demo_event_id: int
):
    print("Executing utils.database.create_demo()...")
    demo_event = db.session.get(DemoEvent, demo_event_id)
    if demo_event:
        demo = Demo(name=name, demo_event_id=demo_event_id)
        db.session.add(demo)
        db.session.commit()
        print("Successfully created demo:", demo.serialize())
    else:
        print("Demo event not found.")
    return demo.id
