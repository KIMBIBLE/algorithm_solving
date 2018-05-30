'''
1) elgamal_pks_genkey(key_length)
- it takes a key bit length and returns a private key sk and a public key pk.
2) elgamal_pks_sign(m, sk, pk)
- it takes a message m with a private key sk and returns a signature sig.
3) elgamal_pks_verify(sig, m, pk)
- it outputs 1 if the signature is valid or 0 otherwise.

To select a primitive root g (or generator), you first select a random element
a such that 1<= a <= p-1 and then sets g = a^2 mod p as a primeitive root.

The report should contain the results of the following examples for
each key_length = 256, 512, and 1024:

>> key_length = 512
>> sk, pk = elgamal_pks_genkey(key_length)
>> m = 1234
>> sig = elgamal_pks_sign(m, sk, pk)
>> elgamal_pks_verify(sig, m, pk)

'''

def check(n):
    k=1
    m=0
    while 1:
        if n%(2**k) == 0:
            k = k+1
        else:
            k = k-1
            m = n//(2**k)
            break

    return k,m

# a : base
# e : exponent
# n : modulus value
def mod_exp(a, e, n):
    tmp = a
    length = 0
    bList = []
    tot = 1

    # convert exponent value to binary string
    while True:
        if (e < 2):
            bList.append(e)
            break
        bList.append(e%2)
        e = e // 2

    length = len(bList)
    for i in range(0, length):
        if bList[i] == 1:
            tot = tot * tmp
            tot = tot % n
        tmp = tmp ** 2
        tmp = tmp % n
    return tot

def ext_gcd(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    return (lastX, lastY)


def miller_rabin_test(n,a,m,k):
    if(mod_exp(a,m,n)==1 or mod_exp(a,m,n)==n-1):
        return 1
    for i in range(1,k):
        if(mod_exp(a,(2**i)*m,n)==n-1):
            return 1
    return 0


def is_prime(n) :

    import random
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




def gcd(ra,rb):
    rc=1
    ora = ra
    orb = rb
    while 1 :
        qa = ra/rb
        rc = ra%rb
        if(rc==0):
            break

        else:
            ra = rb
            rb = rc

    return rb




def elgamal_pks_genkey(key_length):
    print("[*] Elgamal PKS key generating...")
    print("[*] key_length : ",key_length)

    while(1):
        p = random.randint(2**(key_length-1),2**((key_length)))

        if(is_prime(p)==1):
            break;

    x = random.randint(1,2**(key_length-1))

    g = x ** 2 % p


    a = random.randint(1,p-1)
    beta = mod_exp(g,a,p)


    print("[*] Elgamal PKS key generated")
    return a,(p,g,beta)


def elgamal_pks_sign(m,sk,pk) :
    p = pk[0]
    alpha = pk[1]
    bete = pk[2]

    print("[*] Elgamal PKS signing...")
    while(1):
        k = random.randint(1,p-1)
        if(k!=p-1):
            if(gcd(k,p-1)==1):
                break;

    r = mod_exp(alpha,k,p)
    kInverse,temp = ext_gcd(k,p-1)

    while(kInverse<0):
       kInverse = kInverse + (p-1)

    s = kInverse % (p-1)
    s = s*(m-sk*r) % (p-1)


    print("[*] Elgamal PKS sigining Done")
    return (r,s)


def elgamal_pks_verify(sig, m, pk):
    r = sig[0]
    s = sig[1]
    p = pk[0]
    alpha = pk[1]
    beta = pk[2]
    print("[*] Elgamal PKS Verifying...")
    versebeta,tempB = ext_gcd(beta,p)

    while(versebeta<0):
        versebeta = versebeta+p

    modalpha = mod_exp(alpha,m,p)
    modbeta = mod_exp(versebeta,r,p)
    result1 = (modalpha*modbeta)%p
    result2 = mod_exp(r,s,p)
    if result1 == result2:
        print("[*] Elgamal PKS Verify Success")
        return 1;
    else:
        print("[*] Elgamal PKS Verify Fail")
        return 0;


import random

key_length = [2**8, 2**9, 2**10]
sk, pk = elgamal_pks_genkey(key_length[random.randint(0,2)])

print("[*] sk = " ,sk)
print("[*] pk = " ,pk)

m = 1234
sig = elgamal_pks_sign(m,sk,pk)
elgamal_pks_verify(sig,m,pk)
