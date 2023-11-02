#!/usr/bin/python3


def infinite_add(argv):
    nums = [int(x) for x in argv[1:]]
    print(sum(nums))
    return


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
