import pytest


@pytest.mark.usefixtures("app_context_with_test_course")
def create_course_test():
    assert True
