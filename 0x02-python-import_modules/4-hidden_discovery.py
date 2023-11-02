#!/usr/bin/python3
import hidden_4 as h
if __name__ == "__main__":
    x = dir(h)
    s = sorted(y for y in x if not y.startswith("__"))
    for i in s:
        print(i)
