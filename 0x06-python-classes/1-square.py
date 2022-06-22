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
            raise TypeError("The size of the Square must be an int")

        if(size < 0):
            raise ValueError("Size must greater or equal than zero")

        self.__size = size
