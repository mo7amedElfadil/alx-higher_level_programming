#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds the peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for i in list_of_integers[1:]:
        if i > peak:
            peak = i
    return peak
