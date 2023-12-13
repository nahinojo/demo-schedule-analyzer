def get_possible_course_attributes(course_details_list):
    instructors = {}
    course_codes = {}
    terms = {}
    for course_details in course_details_list:
        instructor = course_details["instructors"]
        course_code = course_details["course_code"]
        term = course_details["term"]
        if instructor not in instructors:
            instructors.add(instructor)
        if course_code not in course_codes:
            course_codes.add(course_code)
        if term not in terms:
            terms.add(term)
    possible_course_attributes = {
        "instructors": list(instructors),
        "course_codes": list(course_codes),
        "terms": list(terms)
    }
    return possible_course_attributes

