#!/usr/bin/python3
def c_tenary(C=(), c=""):
    return int(c.find((C[0], C[1])[C[1] in c]))


def no_c(my_string):
    C = ['c', 'C']
    while c_tenary(C, my_string) != -1:
        my_string = (my_string[:c_tenary(C, my_string)] +
                     my_string[c_tenary(C, my_string) + 1:])
        return my_string
