import requests
import os
from icalendar import Calendar

from app import PATH_TO_CALENDAR


def request_calendar():
    """
    Requests the calendar file from Google Calendar.

    Returns
    -------
    calendar: icalendar.Calendar
        The calendar file.
    """
    url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
        ".ics"
    )
    response = requests.get(url)
    os.makedirs(os.path.dirname(PATH_TO_CALENDAR), exist_ok=True)
    with open(PATH_TO_CALENDAR, "wb") as calendar_file:
        calendar_file.write(response.content)
    with open(PATH_TO_CALENDAR) as f:
        calendar = Calendar.from_ical(f.read())
    return calendar
