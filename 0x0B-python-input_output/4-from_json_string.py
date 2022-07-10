#!/usr/bin/python3
"""from_json_string module"""

import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): a Json string to return as an object.
    """
    return json.loads(my_str)
