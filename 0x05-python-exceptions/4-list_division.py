#!/usr/bin/python3
def catch(func, *s):
    result = 0
    try:
        result = func(s[0][s[2]], s[1][s[2]])
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return result


def div(a, b):
    return a / b


def list_division(my_list_1, my_list_2, list_length):
    result = [catch(div, my_list_1, my_list_2, i) for i in range(list_length)]
    return result
