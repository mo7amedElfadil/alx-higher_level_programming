#!/usr/bin/python3
def test_tuple(a):
    if len(a) < 2:
        if len(a) == 1:
            a = (a[0], 0)
        elif not len(a):
            a = (0, 0)
    return a


def add_tuple(tuple_a=(), tuple_b=()):
    a = test_tuple(tuple_a)
    b = test_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])
