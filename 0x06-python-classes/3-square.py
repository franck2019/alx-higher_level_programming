#!/usr/bin/python3

"""
This module defines a Class Square with private attribute size
after validating the size.
"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialize a square

        Args:
           size (int): The size of a side of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """This function hat returns the current square area"""
        return self.__size ** 2
