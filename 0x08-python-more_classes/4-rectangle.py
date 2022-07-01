#!/usr/bin/python3
"""The rectangle module."""


class Rectangle:
    """The class Rectangle."""

    def __init__(self, width=0, height=0):
        """Instanciates a Rectangle object.

        Args:
            width (positive int): The width of the rectangle.
            height (positive int): The height of the rectangle."""

        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    def __str__(self):

        result = ""

        if self.__width == 0 or self.__height == 0:
            return result

        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"

            if i < self.height - 1:
                result += "\n"

        return result

    def __repr__(self):
        """Representation of a rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """Get the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width = value."""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height = value."""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def str(self):

        result = ""

        if self.__width == 0 or self.__height == 0:
            return result

        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"

            if i < self.height - 1:
                result += "\n"

        return result
