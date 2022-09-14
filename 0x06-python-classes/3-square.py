#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Class represents a square"""
    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)
