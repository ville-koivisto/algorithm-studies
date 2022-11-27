"""
A function for counting how many prime numbers there are from 2 to n.

Note: 'for' loops over iterable. If iterable is empty, the body of 'for' is not executed.
Similarly, range returns iterable from start to stop value. If stop is higher than start,
there are no valid values and the iterable is empty. This is why 0 and 1 are skipped
in the function.
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
    print(count_primes(10)) # 4
