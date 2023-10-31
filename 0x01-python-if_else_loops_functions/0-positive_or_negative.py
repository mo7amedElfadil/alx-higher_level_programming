#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} " +
      ("is negative", ("is positive", "is zero")[number == 0])[number >= 0])
