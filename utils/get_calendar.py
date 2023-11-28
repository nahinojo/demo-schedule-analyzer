import requests


def get_calendar():
    url = (
        "https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
        ".ics"
    )
    response = requests.get(url)
    with open("demo-calendar.ics", "wb") as calendar_file:
        calendar_file.write(response.content)
    return
