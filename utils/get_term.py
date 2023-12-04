from datetime import date


def get_term(demo_date, return_end_date=False):
    year = demo_date.year
    winter_end = date(year, 3, 28)
    spring_end = date(year, 6, 14)
    summer_end = date(year, 9, 9)
    if demo_date < winter_end:
        return "Winter"
    elif demo_date < spring_end:
        return "Spring"
    elif demo_date < summer_end:
        return "Summer"
    else:
        return "Fall"
