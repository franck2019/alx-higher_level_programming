#!/usr/bin/python3

for n in range(100):
    if n < 10:
        print(0, end='')

    if n == 99:
        print("{}".format(n), end='\n')

    print("{}".format(n), end=',')
