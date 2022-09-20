#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """ Represents a Rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes private instance attributes: width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Retrieves the private instance attribute: width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter to set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the private instance attribute: height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property setter to set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Prints the rectangle """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """ Returns a string representation of the rectangle """
         w = str(self.__width), 
         h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"
