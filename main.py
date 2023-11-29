import icalendar
import utils

utils.get_calendar()
with open("./demo-calendar.ics") as f:
    calendar = icalendar.Calendar.from_ical(f.read())
for i, event in enumerate(calendar.walk('VEVENT')):
    date_start = event.get("DTSTART").dt
    # if i != 2061:
    #     continue
    if int(date_start.year) >= 2021:
        summary = str(event.get("SUMMARY"))
        is_course = False
        for char in summary:
            if char.isdigit():
                is_course = True
                break
        if not is_course:
            break
        course_code = summary[:summary.find(' ')]
        instructor = summary[summary.find(' ') + 1:]
        description = str(event.get("DESCRIPTION"))
        dissected_description = utils.dissect_description(description)
        demo_event = utils.DemoEvent(
            course_code=course_code,
            instructor=instructor,
            demos=dissected_description[0],
            additional_info=dissected_description[1]
        )

