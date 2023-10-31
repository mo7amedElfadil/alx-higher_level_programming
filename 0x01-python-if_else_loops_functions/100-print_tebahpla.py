#!/usr/bin/python3
for a in reversed(range(97, 123)):
    print("{:c}".format((a, a - 32)[a % 2]), end="")
