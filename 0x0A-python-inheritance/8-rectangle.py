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
