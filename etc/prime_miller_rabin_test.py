import random

def check(n):
    k=1
    m=0
    while True:
        if n%(2**k) == 0:
            k = k+1
        else:
            k = k-1
            m = n//(2**k)
            break

    return k,m
            
        
def mod_exp(a,e,n) :
    tmp = a
    c = []
    total = 1
    length = 0
    j = 0
    while True:
        if(e<2) :
            c.append(e)
            break
        c.append(e%2)
        e = e//2

    length = len(c)

    for j in range(0,length):
        if c[j] == 1:
            total = total*tmp
            total = total%n
        tmp = tmp**2 
        tmp = tmp%n
        
    return total

# b : base 
def miller_rabin_test(n,b,s,t):
    if(mod_exp(b,s,n)==1 or mod_exp(b,s,n)==n-1):
        return 1
    for i in range(1,t):
        if(mod_exp(b,(2**i)*s,n)==n-1):
            return 1
    return 0


def is_prime(n) :
    res = 1
    if n%2 == 0:
        return 0

    k,m = check(n-1)

    for i in range (1,20):
        a = random.randint(1,n-1)
        res = miller_rabin_test(n,a,m,k)
        if res!=1:
            break
        
    return res


print is_prime(561)
print is_prime(569)
print is_prime(2 ** (2 ** 4) + 1)
print is_prime(2 ** (2 ** 10) + 1)
print is_prime(2 ** 1279 - 1)
print is_prime(2 ** 2203 - 1)
print is_prime(2 ** 3217 - 1)