#!/usr/bin/python3

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            prog='2-args',
            description='Prints the number of and the list of its arguments')

    parser.add_argument('argv', nargs='*')

    args = parser.parse_args()

    length = len(args.argv)

    if length == 0:
        print("0 arguments.")
    else:
        text = 'argument'
        print("{} {}:".format(length, text if length == 1 else text + 's'))
        for i in range(length):
            print("{}: {}".format(i + 1, args.argv[i]))
