from datetime import date


def get_quarter(month, day):
    provided_date = date(2024, month, day).isoformat()
    winter_end = date(2024, 3, 28).isoformat()
    spring_end = date(2024, 6, 14).isoformat()
    summer_1_end = date(2024, 7, 30).isoformat()
    summer_full_end = date(2024, 8, 29).isoformat()
    summer_2_end = date(2024, 9, 9).isoformat()
    if provided_date < winter_end:
        return "winter"
    elif provided_date < spring_end:
        return "spring"
    elif provided_date < summer_1_end:
        return "summer_1"
    elif provided_date < summer_full_end:
        return "summer_full"
    elif provided_date < summer_2_end:
        return "summer_2"
    else:
        return "fall"
