#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    calc = __import__("calculator_1")
    print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
