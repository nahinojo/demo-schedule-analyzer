import requests
import os

from app import PATH_TO_CALENDAR


def request_calendar():
    """
    Requests the calendar file from Google Calendar.

    Returns
    -------
    None
    """
    url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
        ".ics"
    )
    response = requests.get(url)
    os.makedirs(os.path.dirname(PATH_TO_CALENDAR), exist_ok=True)
    with open(PATH_TO_CALENDAR, "wb") as calendar_file:
        calendar_file.write(response.content)
    return
