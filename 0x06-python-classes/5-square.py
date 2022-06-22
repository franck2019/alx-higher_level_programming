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
           size (int): The size of a side of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """This function returns the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the new value of a square

        Args:
            value (int): the new value of the square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #
        if size is equal to 0, print an empty line.
        """

        ss = self.__size  # ss means square size

        if ss == 0:
            print()
        else:
            for i in range(ss):

                for j in range(ss):
                    print("#", end="")

                print()
