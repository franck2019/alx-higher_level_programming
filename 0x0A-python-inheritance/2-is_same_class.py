#!/usr/bin/python3
"""same_object module"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class ; otherwise False

    Args:
        obj (:obj): an object
        a_class: a class
    """
    return type(obj) is a_class
