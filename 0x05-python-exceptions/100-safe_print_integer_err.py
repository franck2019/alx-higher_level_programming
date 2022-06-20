#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    ok = False
    try:
        print("{:d}".format(value), end="\n")
        ok = True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)

    return ok
