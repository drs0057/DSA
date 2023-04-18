def factorial(num):
    """Calculate the factorial of a given number."""

    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(3))