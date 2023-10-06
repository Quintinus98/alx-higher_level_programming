#!/usr/bin/python3

def main():
    for path in sorted(dir(hidden_4)):
        if path[0] != "_":
            print("{}".format(path))


if __name__ == "__main__":
    import hidden_4
    main()
