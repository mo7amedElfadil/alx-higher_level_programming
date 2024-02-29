#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """def doc"""
    lst = list_of_integers
    if lst:
        lf = 0
        r = len(lst) - 1
        while lf < r:
            m = (lf + r) // 2
            if lst[m] > lst[m + 1]:
                r = m
            else:
                lf = m + 1
        return lst[lf]
