""" A recursive function for checking if a positive integer is a power of two.

    - Base case: smallest possible power of non-negative value == 1
    - If n meets the base case, stop recursion and return true
    - Check if the remainder for n divided by 2 is zero
    - If so, call the function again with a floor division of n
    - If not, return false
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
