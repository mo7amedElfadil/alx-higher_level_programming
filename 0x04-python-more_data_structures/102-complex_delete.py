#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(filter(lambda x: a_dictionary[x] == value, a_dictionary)):
        del a_dictionary[key]
    return a_dictionary
