#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print(f"The last digit of {number:d} is {last:d} and " +
      (("is less than 6 and not 0", "is 0")[last == 0],
       "is greater than 5")[last > 5])
