"""
Custom exceptions.
"""


class DatabaseStillInitializedException(Exception):
    """
    Database is initialized.
    """
    pass


class DatabaseNotInitializedException(Exception):
    """
    Database is not initialized.
    """
    pass
