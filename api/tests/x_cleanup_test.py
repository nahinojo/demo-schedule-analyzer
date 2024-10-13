"""
Tests application under all configurations.
"""
from app.exceptions import (
    DatabaseIsInitializedException,
    DatabaseIsNotInitializedException
)


def cleanup_test():
    """
    Cleanup test.
    """
    try:
        from app.database import Database
        _session = Database.get_session()
        _engine = Database.get_engine()
        assert _session is not None
        assert _engine is not None
    except DatabaseIsNotInitializedException:
        pass
    else:
        raise DatabaseIsInitializedException(
            "cleanup test failed: Database should not be initialized"
        )
