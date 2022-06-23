#!/usr/bin/python3
import math

"""The magic Module."""


class MagicClass:

    def __init__(self, radius):

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius


"""
import dis


dis.dis(MagicClass)
"""
