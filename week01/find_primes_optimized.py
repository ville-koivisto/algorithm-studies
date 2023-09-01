import math

prime_list = [2]

def find_primes(n):
    if n < 3:
        return prime_list
    for i in range (3,n+1,2):
        for p in prime_list:
            if i%p == 0:
                break
        if i%2 == 0:
            continue
        upper_lim = int(math.sqrt(n)+1)
        for j in range(3, upper_lim, 2):
            if i%j == 0:
                continue
        prime_list.append(i)
    return prime_list

if __name__ == "__main__":
    for p in find_primes(1000):
        print(p)
