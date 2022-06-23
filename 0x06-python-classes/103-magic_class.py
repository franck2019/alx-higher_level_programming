#!/usr/bin/python3

"""The magic Module."""


import math


class MagicClass:
    """This class defines a circle.

    Attributes:
    __radius(int or float): The radius of the circle (private).
    """
    def __init__(self, radius):
        """Initializes a circle.

        Args:
            radius(int or float): the radius of the circle.
                if radius is not an integer or a float number,
                it will raise a TypeError message radius must be a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.__radius


"""
import dis


dis.dis(MagicClass)
"""
