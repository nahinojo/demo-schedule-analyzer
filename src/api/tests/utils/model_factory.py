from models import Course, Demo, DemoEvent

from datetime import date


class ModelFactory:
    @staticmethod
    def create_demo(
            name: str = "DEMO_NAME_TEST",
    ):
        return Demo(name=name)

    @staticmethod
    def create_demo_event(
            event_date: date = date(2000, 1, 1),
            additional_info: str = "ADDITIONAL_INFO_TEST",
            demos: list[Demo] = None
    ):
        if not demos:
            demos = [ModelFactory.create_demo()]
        return DemoEvent(
            event_date=event_date,
            additional_info=additional_info,
            demos=demos
        )

    @staticmethod
    def create_course(
            course_code: str = "COURSE_CODE_TEST",
            instructor: str = "INSTRUCTOR_TEST",
            term: str = "TERM_TEST",
            year: int = 2000,
            demo_events: list[DemoEvent] = None,
    ):
        if not demo_events:
            demo_events = [ModelFactory.create_demo_event()]
        return Course(
            course_code=course_code,
            instructor=instructor,
            term=term,
            year=year,
            demo_events=demo_events
        )
