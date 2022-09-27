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
    
    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
