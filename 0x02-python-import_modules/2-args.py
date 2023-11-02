#!/usr/bin/python3


def print_args(argv):
    argc = len(argv) - 1
    if not argc:
        print("{} arguments.".format(argc))
        return
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))
    for i, arg in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, arg))
    return


if __name__ == "__main__":
    import sys
    print_args(sys.argv)
