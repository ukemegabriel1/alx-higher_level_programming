#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last = int(num_str[-1])
positive = int(num_str) / -1

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last > 0 and positive > 0:
    last *= -1
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
