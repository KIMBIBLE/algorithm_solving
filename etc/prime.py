from math import sqrt
import random

def is_prime(n):
    if n <= 2:
        return True

    sq = int(sqrt(10))
    for x in range(2, sq+1):
        if n % x == 0:
            return False
    
    return True

def generate_all_primes(n):
    l = []
    for x in range(2, n+1):
        if is_prime(x):
            l.append(x)
    return l

def generate_random_prime(a,b):
    l = []
    for x in range(a, b+1):
        if is_prime(x):
            l.append(x)
    return random.choice(l)


print generate_all_primes(200)
print generate_random_prime(100, 200)
