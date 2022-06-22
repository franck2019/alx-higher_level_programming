#!/usr/bin/python3

"""
This module defines a Class Square with private attribute size
after validating the size.
"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square

        Args:
           size (int): The size of a side of the square.
                His default value is 0.
           position (int, int): A tuple of two positive integers representing
                position of the square. His default value is (0, 0).
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not (isinstance(position, tuple) and
                isinstance(position[0], int) and
                isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

        position should be use by using space - Don’t fill lines
        by spaces when position[1] > 0
        """

        ss = self.__size  # ss means square size
        space_before_loop = (self.__position)[1]
        space_in_loop = (self.__position)[0]

        if ss == 0:
            print()
        else:
            print("\n" * space_before_loop, end="")

            for i in range(ss):
                for k in range(space_in_loop):
                    print(end=" ")

                for j in range(ss):
                    print("#", end="")

                print()

    @property
    def position(self):
        """Retrieve the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the new position of the square

        Args:
            value (int, int): A tuple of 2 positives representing
                    the new position of the square.
        """

        if not (isinstance(value, tuple) and
                isinstance(value[0], int) and
                isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
