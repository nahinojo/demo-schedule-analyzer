import pytest


@pytest.mark.usefixtures("app_context")
def init_app_context_test():
    assert False
