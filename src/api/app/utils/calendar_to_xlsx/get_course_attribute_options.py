def get_course_attribute_options(course_details_list):
    """
    Gets the union set of every course attribute (instructor, course code, and
    term) in the course details list.

    Parameters
    ----------
    course_details_list: list
        The list of course details.

    Returns
    -------
    dict
        The dictionary of course attribute options.
    """
    instructors = set()
    course_codes = set()
    terms = set()
    for course_details in course_details_list:
        instructor = course_details["instructor"]
        course_code = course_details["course_code"]
        term = course_details["term"]
        if instructor not in instructors:
            instructors.add(instructor)
        if course_code not in course_codes:
            course_codes.add(course_code)
        if term not in terms:
            terms.add(term)
    course_attribute_options = {
        "instructors": list(instructors),
        "course_codes": list(course_codes),
        "terms": list(terms)
    }
    return course_attribute_options
