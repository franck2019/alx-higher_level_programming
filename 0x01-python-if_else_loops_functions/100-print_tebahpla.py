#!/usr/bin/python3

i = 0
for j in 'abcdefghijklmnopqrstuvwxyz'[::-1]:
    print("{}".format(j if i % 2 == 0 else j.upper()), end='')
    i += 1
