"""
Tests application under all configurations.
"""
import os
import pytest


@pytest.mark.parametrize("env", [
    'testing',
    'production',
    'development'
])
def config_test(app, env):
    """
    Parametrized test to validate app config in different environments.
    """
    flask_app = app(env)
    assert flask_app.config['APP_ENV'] == env
