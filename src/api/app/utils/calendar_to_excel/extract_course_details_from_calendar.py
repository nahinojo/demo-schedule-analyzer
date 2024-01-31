from datetime import date

from app.models import (
    Course,
    DemoEvent,
)
from app.utils import (
    dissect_description,
    get_course_term,
    is_broken_event,
    is_similar_strings,
    request_calendar
)


def extract_course_details_from_calendar(
        target_course_code: str = None,
        target_instructor: str = None,
        target_term: str = None,
        target_year: int = 2023,
        is_target_year_as_minimum: bool = True
):
    """
    Requests the demo calendar from Google and parses the events. It constructs Course objects from the events,
    and returns them in one large list.

    Paramaters
    ----------
    target_course_code: str
        The target course code.
    target_instructor: str
        The target instructor.
    target_term: str
        The target term.
    target_year: int
        The target year.
    is_target_year_as_minium: bool
        Whether the target year is the minimum year.
    is_request_new_calendar: bool
        Whether to request a new calendar.

    Returns
    -------
    all_courses: list
        List of all extracted Course objects.
    """
    calendar = request_calendar()
    all_courses = []
    for calendar_event in calendar.walk("VEVENT"):
        summary = str(calendar_event.get("SUMMARY"))
        demo_datetime = calendar_event.get("DTSTART").dt
        is_not_course = any(c.isdigit() for c in summary)
        if is_not_course:
            continue
        demo_date = date(
            year=demo_datetime.year,
            month=demo_datetime.month,
            day=demo_datetime.day
        )
        instructor = summary[summary.find(" ") + 1:].strip()
        year = demo_date.year
        course_code = summary[: summary.find(" ")]
        term = get_course_term(demo_date)
        description = str(calendar_event.get("DESCRIPTION"))
        demos, additional_information = dissect_description(description)

        is_no_instructor = any(char.isdigit() for char in instructor)
        is_discussion = is_similar_strings("discussion", instructor.lower())
        is_broken = is_broken_event(demo_date, instructor)
        is_not_target_instructor = target_instructor not in {None, instructor}
        is_not_target_year = year >= target_year if is_target_year_as_minimum else year == target_year
        is_not_target_course_code = target_course_code not in {None, course_code}
        is_not_target_term = target_term not in {None, term}
        is_skip_event = any(
            [
                is_no_instructor,
                is_discussion,
                is_broken,
                is_not_target_instructor,
                is_not_target_year,
                is_not_target_course_code,
                is_not_target_term
            ]
        )
        if is_skip_event:
            continue

        new_demo_event = DemoEvent(
            event_date=demo_date,
            demos=demos,
            additional_information=additional_information,
        )
        is_demo_event_in_existing_course = False
        for course in all_courses:
            is_demo_event_in_existing_course = (
                    instructor == course.instructor
                    and course_code == course.course_code
                    and year == course.year
                    and term == course.term
            )
            # Calendar events are inherently sorted by creation date, not occurrence date.
            # This ensures the Courses.demo_events are sorted by occurrence date.
            if is_demo_event_in_existing_course:
                demo_event_list = course.demo_events
                latest_demo_event_date = course.demo_events[-1].event_date
                new_demo_event_date = new_demo_event.event_date
                if new_demo_event_date > latest_demo_event_date:
                    demo_event_list.append(new_demo_event)
                    break
                else:
                    for curr_demo_idx, curr_demo_event in enumerate(demo_event_list):
                        if new_demo_event_date < curr_demo_event.date:
                            demo_event_list.insert(curr_demo_idx, new_demo_event)
                            break
                    break
        if not is_demo_event_in_existing_course:
            new_course = Course(
                course_code=course_code,
                year=year,
                term=term,
                instructor=instructor,
                demo_events=[new_demo_event]
            )
            all_courses.append(new_course)
    return all_courses
