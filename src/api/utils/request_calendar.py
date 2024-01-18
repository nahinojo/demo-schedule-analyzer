import requests
import os


def request_calendar(calendar_path):
    url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
        ".ics"
    )
    response = requests.get(url)
    os.makedirs(os.path.dirname(calendar_path), exist_ok=True)
    with open(calendar_path, "wb") as calendar_file:
        calendar_file.write(response.content)
    return
