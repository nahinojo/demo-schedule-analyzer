import icalendar
import requests

url = ("https://calendar.google.com/calendar/ical/7k8ivkgvm0pgtta67pfafecqmg%40group.calendar.google.com/public/basic"
       ".ics")
response = requests.get(url)
calendar_name = "demo-calendar.ics"
with open(calendar_name, "wb") as f:
    f.write(response.content)
calendar_path = f"./{calendar_name}"
with open(calendar_path) as f:
    calendar = icalendar.Calendar.from_ical(f.read())
for event in calendar.walk('VEVENT'):
    print(event.get("SUMMARY"))
    date_start = event.get("DTSTART").dt
    print(date_start)
    break