def power(num, exp):
    """Calculate num to the power of exp."""
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/num * power(num, exp +1)
    else:
        return num * power(num , exp - 1)

print(power(2, 4))
print(power(2, -2))