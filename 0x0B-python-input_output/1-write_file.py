#!/usr/bin/python3
"""write_file module."""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
        returns the number of characters written.

    Args:
        filename (str): the path to a filename.

    Returns:
        nb_char (int): the number of characters written
    """
    if filename != "" and type(filename) == str:
        with open(filename, 'w', encoding='utf-8') as f:
            nb_char = f.write(text)

    return nb_char
