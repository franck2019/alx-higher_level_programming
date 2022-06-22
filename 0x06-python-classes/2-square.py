#!/usr/bin/python3

"""
This module defines a Class Square with private attribute size after\nvalidating the size.
"""


class Square:
    """a class Square that defines a square."""

    def __init__(self, size=0):
        """The constructor of the square class

        Args:
           size (int): The size of a side of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
