#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

result_of_modulo = number % 10 if number > 0 else -1 * (-number % 10)

if result_of_modulo > 5:
    print(f"Last digit of {number} is {result_of_modulo} and is greater than 5")
elif result_of_modulo < 6:
    print(f"Last digit of {number} is {result_of_modulo} and is less than 6 and not 0")
elif result_of_modulo == 0:
    print(f"Last digit of {number} is {result_of_modulo} and is 0")
