#!/usr/bin/python3


def uniq_add(my_list=[]):

    res = my_list.copy()

    if res:
        res = list(set(res))

    return sum(res)
