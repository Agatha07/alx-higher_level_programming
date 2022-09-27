#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """
    A class with public instance method area()
    """
    def area(self):
        """
        Raises an exception error with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
