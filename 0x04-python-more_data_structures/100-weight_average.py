#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list == []:
        return 0

    total_score_times_weight = sum(list(map(lambda x: x[0] * x[1], my_list)))
    sum_weight = sum(list(map(lambda x: x[1], my_list)))
    weight_avg = total_score_times_weight / sum_weight

    return weight_avg
