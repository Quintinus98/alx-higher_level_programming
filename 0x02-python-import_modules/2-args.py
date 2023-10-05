#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)

    # Conditions for initial print.
    if n == 1:
        print("{:d} argument.".format(n - 1), end="\n")
    elif n == 2:
        print("{:d} argument:".format(n - 1), end="\n")
    else:
        print("{:d} arguments:".format(n - 1), end="\n")

    # Loop from 1 to n
    for i in range(1, n):
        print("{:d}: {}".format(i, sys.argv[i]), end="\n")


if __name__ == "__main__":
    main()
