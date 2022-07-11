#!/usr/bin/python3
"""save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (:obj): The object to save
        filename (str): The path to file to save my_obj in.

    Return:
        Always nothing."""
    if filename != "" and type(filename) is str:
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(my_obj, f)
