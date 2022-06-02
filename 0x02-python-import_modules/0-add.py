#!/usr/bin/python3
from add_0 import add


def print_sum():
    a = 1
    b = 2
    c = add(a, b)
    print(f"{a} + {b} = {c}")

if __name__ == "__main__":
    print_sum()
