#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = clean_tuple(tuple_a)
    tuple_b = clean_tuple(tuple_b)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


def clean_tuple(tuple_x=()):

    if len(tuple_x) > 2:
        return (tuple_x[0], tuple_x[1])

    elif len(tuple_x) < 2:

        if len(tuple_x) == 0:
            return (0, 0)
        else:
            return (tuple_x[0], 0)

    else:
        return tuple_x
