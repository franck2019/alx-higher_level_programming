#!/usr/bin/python33


def safe_print_integer(value):

    try:
        print("{:d}".format(value), end="\n")
    except ValueError:
        return False

    return True
