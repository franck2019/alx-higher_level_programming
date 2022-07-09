#!/usr/bin/python3
"""my_int module."""


class MyInt(int):
    """The class MyInt."""

    def __init__(self, number):
        """Creates a new instance of MyInt.

        Args:
            number (int): the number.

        Return:
            Always nothing.
        """
        super().__init__()
        self.number = number

    def __eq__(self, value):
        """Checks if self.__size != value"""
        return self.number != value

    def __ne__(self, value):
        """Checks if self.__size == value"""
        return not self.__eq__(value)
