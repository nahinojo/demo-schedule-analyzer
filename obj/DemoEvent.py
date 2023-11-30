class DemoEvent:
    def __init__(
            self,
            course_code,
            instructor,
            year,
            month,
            day,
            demos,
            additional_info
    ):
        self.course_code = course_code
        self.instructor = instructor
        self.year = year
        self.month = month
        self.day = day
        self.demos = demos
        self.additional_info = additional_info

