import math


def date_difference_school_weeks(prev_date, next_date):
    """
    Calculates the number of school weeks between two dates.

    Parameters
    ----------
    prev_date: datetime.date
        The previous, earlier date.
    next_date: datetime.date
        The next, later date.

    Returns
    -------
    int
        The number of school weeks between the two dates.
    """

    if next_date is not None:
        curr_date_weekday = next_date.weekday()
        prev_date_weekday = prev_date.weekday()
        curr_date_total_day = next_date.timetuple().tm_yday
        prev_date_total_day = prev_date.timetuple().tm_yday
        date_difference_weeks = (curr_date_total_day - prev_date_total_day) / 7
        is_atleast_one_school_week_apart = (
                curr_date_weekday < prev_date_weekday
                or date_difference_weeks >= 1
        )
        if is_atleast_one_school_week_apart:
            if curr_date_weekday < prev_date_weekday:
                return math.ceil(date_difference_weeks)
            else:
                return math.floor(date_difference_weeks)
    return 0
