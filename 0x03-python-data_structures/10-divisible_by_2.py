#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    def is_even(n):
        return (True, False)[n % 2]
    return list(map(is_even, my_list))
