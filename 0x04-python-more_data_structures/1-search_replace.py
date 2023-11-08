#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list((x, replace)[x == search] for x in my_list)
