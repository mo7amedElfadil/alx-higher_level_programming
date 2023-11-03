#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if len(my_list[1:]) < idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
