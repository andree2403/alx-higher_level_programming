#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    int result == 0
    for i in range(count):
        result = result + int(sys.argv[i + 1])
        print("{}".format(result))
