"""Implement an algorithm to determine if a list has all unique characters."""

import random

list = [random.randint(1, 100) for i in range(20)]
print(list)

def detect_duplicates(list):
    for num in list:
        list.remove(num)
        if num in list:
            print(f"There is a duplicate number: {num}")
            return

    print("All numbers are unique.")

detect_duplicates(list)