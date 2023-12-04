from utils import (
    get_calendar,
    dissect_description,
    get_term,
    date_difference_school_weeks,
)
from icalendar import Calendar
from openpyxl import Workbook
from copy import deepcopy
from datetime import date

MIN_YEAR = 2023
BUILD_PATH = "./build"
CALENDAR_FILE_NAME = "demo-calendar.ics"
SCHEDULE_FILE_NAME = "demo-schedule.xlsx"
CALENDAR_PATH = f"{BUILD_PATH}/{CALENDAR_FILE_NAME}"
SCHEDULE_PATH = f"{BUILD_PATH}/{SCHEDULE_FILE_NAME}"
COURSE_DETAILS = {
    "instructor": str,
    "course_code": str,
    "year": int,
    "term": str,
    "demo_events": [],
}
get_calendar(calendar_path=CALENDAR_PATH)
with open(f"{BUILD_PATH}/{CALENDAR_FILE_NAME}") as f:
    calendar = Calendar.from_ical(f.read())
course_details_list = []
for i, event in enumerate(calendar.walk("VEVENT")):
    demo_datetime = event.get("DTSTART").dt
    demo_date = date(
        year=demo_datetime.year, month=demo_datetime.month, day=demo_datetime.day
    )
    year = demo_date.year
    if year >= MIN_YEAR:
        summary = str(event.get("SUMMARY"))

        # Only analyze course-specific events, which contain a numeric course code.
        is_course = False
        for char in summary:
            if char.isdigit():
                is_course = True
                break
        if not is_course:
            continue

        instructor = summary[summary.find(" ") + 1 :]
        course_code = summary[: summary.find(" ")]
        description = str(event.get("DESCRIPTION"))
        demos, additional_info = dissect_description(description)
        term = get_term(demo_date)
        new_demo_event = {
            "date": demo_date,
            "demos": demos,
            "additional_info": additional_info,
        }
        is_in_existing_course = False
        for course_details in course_details_list:

            is_in_existing_course = (
                instructor == course_details["instructor"]
                and course_code == course_details["course_code"]
                and year == course_details["year"]
                and term == course_details["term"]
            )
            if is_in_existing_course:
                demo_events = course_details["demo_events"]
                latest_demo_event_date = course_details["demo_events"][-1]["date"]
                new_demo_event_date = new_demo_event["date"]
                if new_demo_event_date > latest_demo_event_date:
                    demo_events.append(new_demo_event)
                    break
                else:
                    for curr_demo_idx, curr_demo_event in enumerate(demo_events):
                        curr_demo_event_date = curr_demo_event["date"]
                        if new_demo_event_date < curr_demo_event_date:
                            demo_events.insert(curr_demo_idx, new_demo_event)
                            break
                    break

            print(20 * " - ")
        if not is_in_existing_course:
            course_details = deepcopy(COURSE_DETAILS)
            course_details["instructor"] = instructor
            course_details["course_code"] = course_code
            course_details["year"] = year
            course_details["term"] = term
            course_details["demo_events"].append(new_demo_event)
            course_details_list.append(course_details)


wb = Workbook()
for course_details in course_details_list:
    print(20 * ' - ')
    print("course_details:", course_details)
    ws = wb.create_sheet(
        title=(
            f"{course_details['course_code']}"
            f" {course_details['instructor']}"
            f" - {course_details['term']}"
            f" {course_details['year']}"
        )
    )
    earliest_demo_event_date = course_details["demo_events"][0]["date"]
    latest_demo_event_date = course_details["demo_events"][-1]["date"]
    print("earliest_date:", earliest_demo_event_date)
    print("latest_date:", latest_demo_event_date)
    schedule_span_school_weeks = date_difference_school_weeks(latest_demo_event_date, earliest_demo_event_date)
    print("schedule_span_school_weeks:", schedule_span_school_weeks)

    term = course_details["term"]
    school_weeks_in_term = 11
    school_week_start = 1
    if term == "fall":
        school_weeks_in_term = 12
        school_week_start = 0
    elif (term == "summer_1") or (term == "summer_2"):
        school_weeks_in_term = 6
wb.save(SCHEDULE_PATH)
