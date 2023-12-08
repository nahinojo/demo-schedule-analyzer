from icalendar import Calendar
from datetime import date
from utils import (
    request_calendar,
    dissect_description,
    get_course_term,
    is_broken_event
)

DOWNLOAD_PATH = "./downloads"
CALENDAR_FILE_NAME = "demo-calendar.ics"
CALENDAR_PATH = f"{DOWNLOAD_PATH}/{CALENDAR_FILE_NAME}"


def parse_calendar(
        target_course_code: str = None,
        target_instructor: str = None,
        target_term: str = None,
        target_year: int = 2023,
        is_target_year_as_minium: bool = True,
):
    request_calendar(calendar_path=CALENDAR_PATH)
    with open(CALENDAR_PATH) as f:
        calendar = Calendar.from_ical(f.read())
    course_details_list = []
    for calendar_event in calendar.walk("VEVENT"):
        summary = str(calendar_event.get("SUMMARY"))
        # Only analyze course-specific calendar events, which contain a numeric course code.
        is_course = False
        for char in summary:
            if char.isdigit():
                is_course = True
                break
        if not is_course:
            continue
        demo_datetime = calendar_event.get("DTSTART").dt
        demo_date = date(
            year=demo_datetime.year,
            month=demo_datetime.month,
            day=demo_datetime.day
        )
        instructor = summary[summary.find(" ") + 1:]
        if is_broken_event(demo_date, instructor):
            continue
        if target_instructor not in {None, instructor}:
            continue
        year = demo_date.year
        if is_target_year_as_minium:
            is_course_in_year = year >= target_year
        else:
            is_course_in_year = year == target_year
        if not is_course_in_year:
            continue
        course_code = summary[: summary.find(" ")]
        if target_course_code not in {None, course_code}:
            continue
        description = str(calendar_event.get("DESCRIPTION"))
        demos, additional_information = dissect_description(description)
        term = get_course_term(demo_date)
        if target_term not in {term, None}:
            continue
        new_demo_event = {
            "date": demo_date,
            "demos": demos,
            "additional_information": additional_information,
        }
        is_in_existing_course = False
        for course_details in course_details_list:
            is_in_existing_course = (
                    instructor == course_details["instructor"]
                    and course_code == course_details["course_code"]
                    and year == course_details["year"]
                    and term == course_details["term"]
            )
            # Calendar events are inherently sorted by date they were created, not date they actually occur.
            if is_in_existing_course:
                demo_event_list = course_details["demo_event_list"]
                latest_demo_event_date = course_details["demo_event_list"][-1]["date"]
                new_demo_event_date = new_demo_event["date"]
                if new_demo_event_date > latest_demo_event_date:
                    demo_event_list.append(new_demo_event)
                    break
                else:
                    for curr_demo_idx, curr_demo_event in enumerate(demo_event_list):
                        curr_demo_event_date = curr_demo_event["date"]
                        if new_demo_event_date < curr_demo_event_date:
                            demo_event_list.insert(curr_demo_idx, new_demo_event)
                            break
                    break
        if not is_in_existing_course:
            course_details = {
                "instructor": instructor,
                "course_code": course_code,
                "year": year,
                "term": term,
                "demo_event_list": [new_demo_event]
            }
            course_details_list.append(course_details)
    return course_details_list


if __name__ == '__main__':
    print(parse_calendar(
        target_instructor="Krivorotov",
        target_year=2022,
        target_course_code="7E"
    )[0])
