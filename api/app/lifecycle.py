"""
Lifecycle hooks for Flask application.
"""
from flask import g, current_app
from app.database import Database


def register_lifecycle_hooks():
    """
    Registers the database session lifecycle hooks.
    """

    @current_app.before_request
    def before_request():
        """
        Initializes the database session before each request.
        """
        g.db_session = Database.get_session()

    @current_app.teardown_request
    def teardown_request(exception):
        """
        Closes the database session after each request.
        """
        db_session = getattr(g, "db_session", None)
        if db_session is not None:
            db_session.close()
