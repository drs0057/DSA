def gcd(a, b):
    """Find the greatest common divisor between two numbers."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(18, 12))