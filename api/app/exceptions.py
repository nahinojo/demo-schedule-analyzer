"""
Custom exceptions.
"""


class DatabaseIsInitializedException(Exception):
    """
    Database is initialized.
    """
    pass


class DatabaseIsNotInitializedException(Exception):
    """
    Database is not initialized.
    """
    pass
