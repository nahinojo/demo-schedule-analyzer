import requests
import os


def get_calendar(build_path, calendar_file_name):
    file_path = f"{build_path}/{calendar_file_name}"
    url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
        ".ics"
    )
    response = requests.get(url)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as calendar_file:
        calendar_file.write(response.content)
    return
