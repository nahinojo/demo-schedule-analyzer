from utils import get_calendar, dissect_description, get_quarter
from icalendar import Calendar
from openpyxl import Workbook
from copy import deepcopy

MIN_YEAR = 2023
CALENDAR_FILE_NAME = "demo-calendar.ics"
SCHEDULE_FILE_NAME = "demo-schedule.xlsx"
SHEET_DETAILS = {
    "instructor": str,
    "course_code": str,
    "year": int,
    "quarter": str,
    "demo_events": [],
}

wb = Workbook()
ws = wb.active
get_calendar()

with open(f"./{CALENDAR_FILE_NAME}") as f:
    calendar = Calendar.from_ical(f.read())
sheet_details_list = []
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
        for idx, sheet_details in enumerate(sheet_details_list):
            is_course_match = (
                    instructor == sheet_details["instructor"]
                    and course_code == sheet_details["course_code"]
                    and year == sheet_details["year"]
                    and quarter == sheet_details["quarter"]
            )
            if is_course_match:
                sheet_details_list[idx]["demo_events"].append(demo_event)
                break
        if not is_course_match:
            sheet_details = deepcopy(SHEET_DETAILS)
            sheet_details["instructor"] = instructor
            sheet_details["course_code"] = course_code
            sheet_details["year"] = year
            sheet_details["quarter"] = quarter
            sheet_details["demo_events"].append(demo_event)
            sheet_details_list.append(sheet_details)
print(sheet_details_list[0])

wb.save(SCHEDULE_FILE_NAME)
