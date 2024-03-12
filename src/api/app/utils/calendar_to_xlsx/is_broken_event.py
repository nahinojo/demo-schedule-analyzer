from datetime import date


def is_broken_event(event_date, instructor):
    """
    Checks if the calendar event is broken event.

    Some calendar events are "broken" such that they are extraneous yet cannot be removed. They exist within the .ical
    file but cannot be located using the Google Calendar App.

    Parameters
    ----------
    event_date: datetime.date
        The date of the event.
    instructor: str
        The instructor of the event.

    Returns
    -------
    bool
        True if the event is a broken event, False otherwise.1
    """
    broken_event_list = [
        {
            "date": date(2022, 9, 29),
            "instructor": "Krivorotov"
        },
        {
            "date": date(2022, 9, 22),
            "instructor": "Krivorotov"
        },
    ]  # More may exist. Add as needed.
    for broken_event in broken_event_list:
        if event_date == broken_event["date"] and instructor == broken_event["instructor"]:
            return True
    return False
