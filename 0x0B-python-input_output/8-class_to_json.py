#!/usr/bin/python3
"""class_to_json module
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj (obj): the object

    Returns:
        dict (dict): the dictionary description of obj.
    """
    return obj.__dict__
