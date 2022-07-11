#!/usr/bin/python3
"""load_from_json_file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The path to file to data from.

    Return:
        Always nothing."""

    if filename != "" and type(filename) is str:
        with open(filename, 'r', encoding="utf-8") as f:
            result = json.load(f)

        return result
