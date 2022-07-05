#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """This function returns the list of available
     attributes and methods of an object.

    Args:
        obj: an object.
    """
    return dir(obj)
