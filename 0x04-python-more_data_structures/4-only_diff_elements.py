#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    comm = set(x for x in set_1 if x in set_2)
    return set(x for x in set_1.union(set_2) if x not in comm)
