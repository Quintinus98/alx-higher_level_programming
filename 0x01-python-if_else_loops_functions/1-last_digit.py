#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lg = -1 * ((-1 * number) % 10)
else:
    lg = number % 10

if lg > 5:
    print(f"Last digit of {number} is {lg} and is greater than 5")
elif lg == 0:
    print(f"Last digit of {number} is {lg} and is 0")
else:
    print(f"Last digit of {number} is {lg} and is less than 6 and not 0")
