from datetime import date


def is_broken_event(event_date, instructor):
    """
    Determines if provided calendar event is 'broken'.
    Specifically, these events are extraneous but cannot be removed from Google Calendar.
    :param event_date: datetime.date
    :param instructor: string
    :return: bool
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
    ]
    for broken_event in broken_event_list:
        if event_date == broken_event["date"] and instructor == broken_event["instructor"]:
            return True
    return False
