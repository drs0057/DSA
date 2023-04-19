"""Find the missing number in the given list of integers 1 - 100."""

import random

list = [i for i in range(1, 101)]
random_number = random.randint(1, 100)
list.remove(random_number)

print(random_number)
print(list)
print()


def find_missing_num(list):

    sum1 = 100 * 101 / 2
    sum2 = sum(list)
    return sum1 - sum2

print(find_missing_num(list))
