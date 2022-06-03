#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    res = []
    for number in my_list:
        if number % 2:
            res.append(False)
        else:
            res.append(True)

    return res
