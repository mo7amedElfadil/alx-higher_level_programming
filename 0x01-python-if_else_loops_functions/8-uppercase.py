#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format((ord(c), ord(c)-32)[ord(c) in range(97, 123)]),
              end=(""))
    print()
