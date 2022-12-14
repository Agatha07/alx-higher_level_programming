#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes private instance attributes: width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A property setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A property setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrieves the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves the perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Returns a string representation of the Rectangle"""
        sw, sh = str(self.__width), str(self.__height)
        return "Rectangle(" + sw + ", " + sh + ")"
        
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
