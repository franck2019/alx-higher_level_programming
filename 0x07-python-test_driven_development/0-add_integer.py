#!/usr/bin/python3
"""This Module has a function that adds 2 integers.
Prototype: def add_integer(a, b=98):
    - a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer.
    - a and b must be first casted to integers if they are float."""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b.
    Args: a (int): first argument.
          b (int): second argument."""

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('a must be an integer or b must be an integer')

    return int(a) + int(b)
