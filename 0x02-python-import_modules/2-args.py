#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    print("{:d} arguments:".format(n - 1), end="\n")
    for i in range(1, n):
        print("{:d}: {}".format(i, sys.argv[i]), end="\n")


if __name__ == "__main__":
    main()
