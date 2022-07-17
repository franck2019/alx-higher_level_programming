#!/usr/bin/python3
"""stats module: script that reads stdin line by line and computes metrics."""

import sys


def stat_1(a_dict):
    """print the total size of the file per status code"""
    total = 0
    a_dict = dict(sorted(a_dict.items()))
    for code, value in a_dict.items():
        total += value

    print(f"File size: {total}")


def stat_2(a_dict):
    """Print stat for status code and ocurrence"""
    a_dict = dict(sorted(a_dict.items()))
    for key, value in a_dict.items():
        print(f"{key}: {value}")


status_file = {}
status_ocurrence = {}

counter = 0

try:
    while True:
        line = sys.stdin.readline()
        line_1 = tuple(line.split()[-2:])
        status_code, file_size = line_1

        if status_code not in status_file:
            status_file[status_code] = int(file_size)
            status_ocurrence[status_code] = 1
        else:
            status_file[status_code] += int(file_size)
            status_ocurrence[status_code] += 1

        counter += 1  # increment the counter

        if counter == 10:
            stat_1(status_file)
            stat_2(status_ocurrence)
            counter = 0
except KeyboardInterrupt as ki:
    stat_1(status_file)
    stat_2(status_ocurrence)
    print(ki)
