"""
Utilities for testing.
"""
from datetime import datetime


def print_with_timestamp(*args):
    """
    Prints the current timestamp and the arguments.
    """
    str_stmt = "".join([str(arg) for arg in args])
    print(f"[{datetime.now().timestamp()}]: {str_stmt}")
