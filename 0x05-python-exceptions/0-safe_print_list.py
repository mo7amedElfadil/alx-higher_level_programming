#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i, e in enumerate(my_list):
            if i == x:
                i -= 1
                break
            print(e, end="")
        print()
    except Exception:
        return i
    return i + 1
