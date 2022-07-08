#!/usr/bin/python3
"""Rectangle module."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """init function.

        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle.

        Return:
            Always nothing
        """
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the representation of a rectangle:
            [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates the area of a rectangle."""
        return self.__width * self.__height

    def print(self):
        """Prints a rectanglrthe following description:
            [Rectangle] <width>/<height>"""

        print(f"[Rectangle] {self.__width}/{self.__height}")
