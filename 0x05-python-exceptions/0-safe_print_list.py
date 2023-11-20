#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for e in my_list:
            if i == x:
                break
            i += 1
            print(e, end="")
        print()
    except Exception:
        return i
    return i
