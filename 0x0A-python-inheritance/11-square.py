#!/usr/bin/python3
"""Square module."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """init function.

        Args:
            size (int): the size of the square

        Return:
            Always nothing
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the representation of a square:
        [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculates the area of a square."""
        return super().area()
