#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    result = 0
    for i in range(count - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
