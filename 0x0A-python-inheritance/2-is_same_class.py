#!/usr/bin/python3
"""Module 2-is_same_class.
Checks if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class.
    Args:
        - obj: The object to check
        - a_class: class to verify the instance of
    Returns: True if obj is an instance of a specified a_class,
    Otherwise - False
    """

    return True if type(obj) is a_class else False
