import string
import random
from datetime import date, timedelta

from app.models import Course, DemoEvent, Demo


def random_string(length=10,
                  chars=string.ascii_lowercase + string.digits
                  ):
    """
    Generates a random string of the specified length.

    Parameters
    ----------
    length: int
        The length of the string to generate.
    chars: str
        The characters to use in the string.

    Returns
    -------
    str
        The generated string.
    """
    return ''.join(random.choice(chars) for _ in range(length))


def random_date(year: int = date.today().year) -> date:
    """
    Generates a random date.

    Parameters
    ----------
    year: int
        The year to generate the date for.

    Returns
    -------
    date
        The generated date.
    """
    delta = timedelta(days=random.randint(0, 365))
    return date(year=year, month=1, day=1) + delta


def random_term() -> str:
    """
    Generates a random term.

    Returns
    -------
    str
        The generated term.
    """
    return random.choice(["Winter", "Spring", "Summer", "Fall"])


def randome_course_code() -> str:
    """
    Generates a random course code.

    Returns
    -------
    str
        The generated course code.
    """
    course_number: str = str(random.randint(1, 9))
    course_char: str = random.choice(string.ascii_uppercase)
    return f"{course_number}{course_char}"


def random_demo() -> Demo:
    """
    Generates a random demo.

    Returns
    -------
    Demo
        The generated demo.
    """
    return Demo(name=random_string())


def random_demo_event(event_date: date or None = None,
                      additional_information: str or None = None,
                      demos: list[Demo] or None = None,
                      ) -> DemoEvent:
    """
    Generates a random demo event.

    Parameters
    ----------
    demos: Demo
        The demo to associate with the event.
    event_date: date
        The date of the event.
    additional_information: str
        The additional information associated with the event.

    Returns
    -------
    DemoEvent
        The generated demo event.
    """
    if demos and event_date and additional_information:
        raise ValueError(f"Cannot provide all arguments."
                         f"Create DemoEvent manually instead."
                         )

    event_date = event_date or random_date()
    additional_information = additional_information or random_string()
    demos = demos or [random_demo() for _ in range(random.randint(1, 6))]
    return DemoEvent(event_date=event_date,
                     additional_information=additional_information,
                     demos=demos
                     )


def random_course(course_code: str or None = None,
                  instructor: str or None = None,
                  term: str or None = None,
                  year: int or None = None,
                  demo_events: list[DemoEvent] or None = None
                  ) -> Course:
    """
    Generates a random course.

    Parameters
    ----------
    demo_events: DemoEvent
        The demo events to associate with the course.
    course_code: str
        The course code of the course.
    instructor: str
        The instructor of the course.
    term: str
        The term of the course.
    year: int
        The year of the course.

    Returns
    -------
    Course
        The generated course.
    """
    if demo_events and course_code and instructor and term and year:
        raise ValueError(f"Cannot provide all arguments."
                         f"Create Course manually instead."
                         )

    course_code = course_code or randome_course_code()
    instructor = instructor or random_string()
    term = term or random_term()
    year = year or random.randint(2010, 2020)
    demo_events = demo_events or [
        random_demo_event() for _ in range(random.randint(1, 6))
    ]
    return Course(course_code=course_code,
                  instructor=instructor,
                  term=term,
                  year=year,
                  demo_events=demo_events)
