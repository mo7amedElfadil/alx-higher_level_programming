#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list[1:]) < idx < 0:
        return my_list.copy()
    my_list_copy = my_list.copy()
    my_list_copy[idx] = element
    return my_list_copy
