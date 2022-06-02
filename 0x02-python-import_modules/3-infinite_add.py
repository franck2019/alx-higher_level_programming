#!/usr/bin/python3

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            prog='3-infinite_add.py',
            description='Prints the result of the addition of all arguments')

    parser.add_argument('argv', type=int, nargs='*')

    args = parser.parse_args()

    length = len(args.argv)

    if length == 0:
        print("0")
    else:
        print("{}".format(sum(args.argv)))
