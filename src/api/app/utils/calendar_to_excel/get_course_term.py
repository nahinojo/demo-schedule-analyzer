from datetime import date


def get_course_term(event_date):
    """
    Gets the term of the course.

    Parameters
    ----------
    event_date: datetime.date
        The date of the demonstration.

    Returns
    -------
    str
        The term of the course.
    """
    year = event_date.year
    winter_end = date(year, 3, 28)
    spring_end = date(year, 6, 14)
    summer_end = date(year, 9, 9)
    if event_date < winter_end:
        return "Winter"
    elif event_date < spring_end:
        return "Spring"
    elif event_date < summer_end:
        return "Summer"
    else:
        return "Fall"
