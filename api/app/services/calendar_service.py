import os
import requests
import threading
from icalendar import Calendar
from flask import current_app


class CalendarService:
    """
    Calendar Service.

    Attributes
    ----------
    _instance: CalendarService
        Singleton instance of CalendarService.
    _calendar: icalendar.Calendar
        The requested calendar file.
    """
    _instance = None
    _lock = threading.Lock()
    _calendar = None

    def __new__(cls) -> "CalendarService":
        """
        Returns the singleton instance of CalendarService.

        Returns
        -------
        CalendarService
            The singleton instance of CalendarService.
        """
        if cls._instance is None:
            with cls.lock:
                if cls._instance is None:
                    cls._instance = super(CalendarService, cls).__new__(cls)
                    cls._fetch_calendar()
        return cls._instance

    @property
    def lock(self):
        """
        Locks the thread to prevent race conditions when instantiating the
        service and updating the calendar.

        Returns
        -------
        lock: threading.Lock
            The lock object.
        """
        return self._lock

    @property
    def calendar(self) -> Calendar:
        """
        The requested calendar file.

        Returns
        -------
        calendar: icalendar.Calendar
            The demonstration calendar object.
        """
        return self._calendar

    @classmethod
    def _fetch_calendar(cls):
        """
        Updates calendar to the latest version.

        Returns
        -------
        calendar: icalendar.Calendar
            The demonstration calendar object.
        """
        calendar_url = (
            "https://calendar.google.com/calendar/ical"
            "/7k8ivkgvm0pgtta67pfafecqmg%"
            "40group.calendar.google.com/public/basic.ics"
        )
        response = requests.get(calendar_url)
        calendar_file_path = current_app.config["CALENDAR_PATH"]
        os.makedirs(os.path.dirname(calendar_file_path), exist_ok=True)
        with open(calendar_file_path, "wb") as calendar_file:
            calendar_file.write(response.content)
        with open(calendar_file_path) as f:
            calendar = Calendar.from_ical(f.read())
        cls._calendar = calendar
        return
