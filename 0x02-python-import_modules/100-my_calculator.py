#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            prog='./100-my_calculator.py',
            usage='%(prog)s a operator b',
            description='Prints the result of the addition of all arguments')

    parser.add_argument('argv', nargs='*')

    args = parser.parse_args()

    #print(args.argv)

    length = len(args.argv)

    if length != 3:
        print("Usage: {} <a> operator <b>".format(parser.prog))
        exit(1)

    else:

        a = int(args.argv[0])
        operator = args.argv[1]
        b = int(args.argv[2])

        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
