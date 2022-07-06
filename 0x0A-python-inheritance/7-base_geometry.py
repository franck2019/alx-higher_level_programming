#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This function validates the value argument.

        Args:
            name (str):an attribute name
            value (int): the value of the attribute name
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
