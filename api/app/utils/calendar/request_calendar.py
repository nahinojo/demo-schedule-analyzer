"""
Requests the calendar file from Google Calendar.
"""
import os
import requests
from icalendar import Calendar

from flask import current_app


def request_calendar() -> Calendar:
    """
    Requests the calendar file from Google Calendar.

    Returns
    -------
    calendar: icalendar.Calendar
        The requested calendar file.
    """
    calendar_url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%"
        "40group.calendar.google.com/public/basic.ics"
    )
    calendar_file_path = current_app.config["CALENDAR_PATH"]
    response = requests.get(calendar_url)
    os.makedirs(os.path.dirname(calendar_file_path), exist_ok=True)
    with open(calendar_file_path, "wb") as calendar_file:
        calendar_file.write(response.content)
    with open(calendar_file_path) as f:
        calendar = Calendar.from_ical(f.read())
    return calendar
