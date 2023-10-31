#!/usr/bin/python3
def print_last_digit(number):
    last = number % (10, -10)[number < 0]
    last = (last, -last)[last < 0]
    print("{:d}".format(last), end="")
    return last
