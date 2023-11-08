#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    t = {x: y for x, y in a_dictionary.items() if y is not None}
    return max(t, key=t.get)
