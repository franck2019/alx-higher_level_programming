#!/usr/bin/python3
"""append_write module."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
        returns the number of characters added.

    Args:
        filename (str): the path to a filename.
        text (str): the text to add.

    Returns:
        nb_char (int): the number of characters written
    """
    if filename != "" and type(filename) == str:
        with open(filename, 'a', encoding='utf-8') as f:
            nb_char = f.write(text)

    return nb_char
