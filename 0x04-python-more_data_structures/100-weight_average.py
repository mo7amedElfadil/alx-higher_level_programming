#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    for t in my_list:
        score += t[0] * t[1]
        weight += t[1]
    if len(my_list):
        return score / weight
    return 0
