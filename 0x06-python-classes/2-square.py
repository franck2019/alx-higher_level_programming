#!/usr/bin/python3

"""square module"""


class Square:
    """a class Square that defines a square."""

    def __init__(self, size=0):
        """The constructor of the square class

        Args:
           size (int): The size of a side of the square
        """

        if(not isinstance(size, int)):
            raise TypeError("size must be an integer")

        if(size < 0):
            raise ValueError("Size must be >= 0")

        self.__size = size
