from utils import get_calendar, dissect_description, get_quarter
from icalendar import Calendar
from openpyxl import Workbook
from copy import deepcopy
from datetime import datetime

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
    "quarter": str,
    "demo_events": [],
}
get_calendar(
    calendar_path=CALENDAR_PATH
)

with open(f"{BUILD_PATH}/{CALENDAR_FILE_NAME}") as f:
    calendar = Calendar.from_ical(f.read())
course_details_list = []
for i, event in enumerate(calendar.walk("VEVENT")):
    date_start = event.get("DTSTART").dt
    year = date_start.year
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

        instructor = summary[summary.find(" ") + 1:]
        course_code = summary[: summary.find(" ")]
        description = str(event.get("DESCRIPTION"))
        demos, additional_info = dissect_description(description)
        month = date_start.month
        day = date_start.day
        quarter = get_quarter(
            month=month,
            day=day
        )
        demo_event = {
            "month": month,
            "day": day,
            "demos": demos,
            # "additional_info": additional_info,
        }

        is_course_match = False
        for idx, course_details in enumerate(course_details_list):
            is_course_match = (
                    instructor == course_details["instructor"]
                    and course_code == course_details["course_code"]
                    and year == course_details["year"]
                    and quarter == course_details["quarter"]
            )
            if is_course_match:
                course_details_list[idx]["demo_events"].append(demo_event)
                break
        if not is_course_match:
            course_details = deepcopy(COURSE_DETAILS)
            course_details["instructor"] = instructor
            course_details["course_code"] = course_code
            course_details["year"] = year
            course_details["quarter"] = quarter
            course_details["demo_events"].append(demo_event)
            course_details_list.append(course_details)

wb = Workbook()
for course_details in course_details_list:
    ws_title = (
        f"{course_details['instructor']}"
        f" {course_details['course_code']}"
        f" {course_details['quarter']}"
        f" {course_details['year']}"
    )
    ws = wb.create_sheet(title=ws_title)
    schedule_span_weeks = 1
    prev_date = None
    for demo_event in course_details["demo_events"]:
        year = course_details["year"]
        month = course_details["month"]
        day = course_details["day"]
        curr_date = datetime(
            year=year,
            month=month,
            day=day
        )
        if prev_date is not None:
            date_difference_days = curr_date.day - prev_date.day
            if date_difference > 2:
                prev_date_weekday = prev_date.weekday()
                date_weekday = curr_date.weekday()

        prev_date = curr_date


    weeks_in_quarter = 10
    if course_details["quarter"] == "fall":
        weeks_in_quarter = 11
    schedule_start_delay_weeks = 0


print(course_details_list)
wb.save(SCHEDULE_PATH)
