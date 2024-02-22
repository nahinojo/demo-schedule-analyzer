import pytest


@pytest.mark.usefixtures("app_context")
def generate_schedule_test():
    """
    Tests generate_schedule function.
    """
    from app.utils import generate_schedule
    generate_schedule()
    assert True
