#!/usr/bin/python3
"""append_after module."""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing
        a specific string.

    Args:
        filename (str): The file name to insert into
        search_string (str): The string to search for
        new_string (str): the new string to insert

    Returns:
        Always nothing
    """
    # open the file and read all the lines
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()

    # retrieve the position line where search_string appears
    targets = []

    for i in range(len(lines)):
        if search_string in lines[i]:
            targets.append(i)

    # add the new string in all targets position
    j = 0  # offset to add 1 everytime we insert something
    for i in targets:
        lines.insert(i + j + 1, new_string)
        j += 1

    with open(filename, mode='w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
