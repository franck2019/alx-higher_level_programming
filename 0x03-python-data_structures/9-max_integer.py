#!/usr/bin/python3


def max_integer(my_list=[]):

    length = len(my_list)

    if length == 0:
        return None
    else:
        maximum = my_list[0]

        for i in range(1, length):
            if maximum < my_list[i]:
                maximum = my_list[i]

    return maximum
