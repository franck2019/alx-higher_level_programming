#!/usr/bin/python3
"""The rectangle module."""


class Rectangle:
    """The class Rectangle.

    Attributes:
                number_of_instances (int): number of instances
                created from this class. Default 0.
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

    def __str__(self):

        result = ""

        if self.__width == 0 or self.__height == 0:
            return result

        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)

            if i < self.height - 1:
                result += "\n"

        return result

    def __repr__(self):
        """Representation of a rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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
                result += str(self.print_symbol)

            if i < self.height - 1:
                result += "\n"

        return result

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (obj:Rectangle): the first rectangle.
            rect_2 (obj:Rectangle): the second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
