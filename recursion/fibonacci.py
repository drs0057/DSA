def fibonacci_number(index):
    """Input an integer, return the number in the Fib. Seq. at that index"""

    # sanitize input
    assert index >= 0 and isinstance(index, int), "Must be a positive integer."

    # base cases
    if index == 0:
        return 0
    elif index == 1:
        return 1
    
    #recursive
    return fibonacci_number(index - 1) + fibonacci_number(index - 2)

print(fibonacci_number(10))
print(fibonacci_number(-3))