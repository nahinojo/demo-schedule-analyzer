import icalendar
import utils

utils.get_calendar()

with open("./demo-calendar.ics") as f:
    calendar = icalendar.Calendar.from_ical(f.read())
for event in calendar.walk('VEVENT'):
    date_start = event.get("DTSTART").dt
    if int(date_start.year) >= 2021:
        summary = str(event.get("SUMMARY"))
        course_code = summary[:2]
        instructor = summary[3:]
        description = str(event.get("DESCRIPTION"))
        print(description)
        print(100 * '*')
