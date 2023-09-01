"""
A function for counting how many prime numbers there are from 2 to n.
"""

def count_primes (n):
    primes = []
    for i in range(2, n):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)
    return len(primes)


if __name__ == "__main__":
    print(count_primes(10))
