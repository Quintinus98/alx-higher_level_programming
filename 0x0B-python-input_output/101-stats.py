#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


def display_stats(file_size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


def main():
    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for line in sys.stdin:
            if cnt == 10:
                display_stats(file_size, status_codes)
                cnt = 1
            else:
                cnt += 1

            line = line.split()
            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        display_stats(file_size, status_codes)

    except KeyboardInterrupt:
        display_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    import sys
    main()
