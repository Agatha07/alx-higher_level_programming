#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square."""
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** self.__size
  
    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
         if self.__size == 0:
            print("")
