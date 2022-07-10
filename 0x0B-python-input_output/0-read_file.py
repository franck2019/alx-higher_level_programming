#!/usr/bin/python3
"""read_file module."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): the path to a filename.

    Returns:
        Always nothing.
    """
    with open(filename) as f:
        result = f.read()

    print(result)
