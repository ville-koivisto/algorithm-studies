"""
A recursive function for checking if a positive integer is a power of two.
"""

def check_power (n):
    if n == 1:
        return True
    elif n%2 == 0:
        return check_power(n//2)

    return False

if __name__ == "__main__":
    print(check_power(1)) # True
    print(check_power(5)) # False
    print(check_power(8)) # True
    print(check_power(32)) # True
    print(check_power(987)) # False
    print(check_power(1099511627776)) # True
    print(check_power(123456789)) # False
