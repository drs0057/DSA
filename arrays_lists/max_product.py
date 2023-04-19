"""Find maximum product of two integers from an list where all integers are positive."""

import random

list = []
for i in range(20):
    list.append(random.randint(1,100))

def findMaxProduct(list):
    max = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] * list[j] > max:
                max = list[i] * list[j]
    print(max)

print(list)
findMaxProduct(list)