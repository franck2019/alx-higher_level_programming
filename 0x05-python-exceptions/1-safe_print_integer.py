#!/usr/bin/python33


def safe_print_integer(value):

    ok = False
    try:
        print("{:d}".format(value), end="\n")
        ok = True
    except Exception:
        pass

    return ok
