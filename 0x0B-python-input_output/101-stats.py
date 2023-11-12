#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def main():
    f_size = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    i = 0
    try:
        for a_line in sys.stdin:
            tok = a_line.split()
            if len(tok) >= 2:
                a = i
                if tok[-2] in status_code:
                    status_code[tok[-2]] += 1
                    i += 1
                try:
                    f_size += int(tok[-1])
                    if a == i:
                        i += 1
                except FileNotFoundError:
                    if a == i:
                        continue
            if i % 10 == 0:
                print("File size: {:d}".format(f_size))
                for key, val in sorted(status_code.items()):
                    if val:
                        print("{:s}: {:d}".format(key, val))
        print("File size: {:d}".format(f_size))
        for key, val in sorted(status_code.items()):
            if val:
                print("{:s}: {:d}".format(key, val))

    except KeyboardInterrupt:
        print("File size: {:d}".format(f_size))
        for key, val in sorted(status_code.items()):
            if val:
                print("{:s}: {:d}".format(key, val))


main()
