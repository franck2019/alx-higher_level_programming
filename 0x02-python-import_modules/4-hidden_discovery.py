#!/usr/bin/python3

from hidden_4 import *


if __name__ == '__main__':
    for name in dir():
        if name[0] != '_':
            print("{}".format(name))
