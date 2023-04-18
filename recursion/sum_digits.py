def sum_digits(num):
    """Return the sum of the digits of a number using a string."""
    num_str = str(num)
    if len(num_str) == 1:
        return int(num_str[0])
    else:
        return int(num_str[-1]) + sum_digits(int(num_str[:-1]))

print(sum_digits(1234))


def modulus_sum_digits(num):
    """Return the sum of the digits of a number using modulus."""
    if num == 0:
        return 0
    else:
        return num % 10 + modulus_sum_digits(num // 10)

print(modulus_sum_digits(1234))
