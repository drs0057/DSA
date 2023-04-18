def dtb(num):
    """Convert a number from decimal to binary."""
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * dtb(num//2)
    

print(dtb(12345))