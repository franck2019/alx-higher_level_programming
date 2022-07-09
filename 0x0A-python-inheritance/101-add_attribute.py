#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        attr_name (str): the attribute name
        attr_value (any): the attribute value

    N.B: Raise a TypeError exception, with the message can't
    add new attribute if the object can’t have new attribute."""

    if '__dict__' not in dir(obj):
        raise TypeError('can\'t add new attribute')
    else:
        obj.__dict__[attr_name] = attr_value
