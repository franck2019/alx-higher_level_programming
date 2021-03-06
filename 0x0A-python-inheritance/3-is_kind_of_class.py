#!/usr/bin/python3
"""kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class ; otherwise False

    Args:
        obj (:obj): an object
        a_class: a class
    """
    return isinstance(obj, a_class)
