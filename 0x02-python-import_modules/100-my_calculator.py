#!/usr/bin/python3


def my_calc(av):
    from calculator_1 import add, sub, mul, div
    ac = len(av[1:])
    print(ac)
    if ac != 3:
        print(f"Usage: {av[0]} <a> <operator> <b>")
        exit(1)
    a = int(av[1])
    o = av[2]
    b = int(av[3])
    c = {"+": add, "-": sub, "*": mul, "/": div}
    try:
        print("{} {} {} = {}".format(a, o, b, c[o](a, b)))
    except KeyError:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    my_calc(sys.argv)
