'''
Implement the RSA algorithm by using python.
When you submit, you should submit a report file
(rsa.pdf) and a souce file (rsa.py).
The report file should contain a source code and
the running results of your functions in the python shell.
The python source file should contain the souce code of your functions.

1) rsa_genkey(key_length): it takes a key bit length and returns
a private key sk and a public key pk.
2) rsa_encrypt(m, pk): it takes a message m and returns an encrypted
ciphertext ct by using the public key pk.
3) rsa_decrypt(ct, sk): it takes a ciphertext ct and a private eky sk
and outputs a decrypted plaintext m by using the private key sk.

The report should contain the results of the following examples
for each key_length = 256, 512, and 1024:

>> key_length = 1024
>> sk, pk = rsa_genkey(key_length)
>> m = 1234
>> ct = rsa_encrypt(m, pk)
>> m = rsa_decrypt(ct, sk)
'''
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

def crt(p,q,a,b):
    i=1
    j=1

    x,y = ext_gcd(p,q)

    return ((a*q*y) + (b*p*x)) % (p*q)

def miller_rabin_test(n,b,s,t):
    if(mod_exp(b,s,n)==1 or mod_exp(b,s,n)==n-1):
        return 1
    for i in range(1,t):
        if(mod_exp(b,(2**i)*s,n)==n-1):
            return 1
    return 0


def is_prime(n):
    res = 1
    if n%2 == 0:
        return False

    k,m = check(n-1)

    for i in range (1,20):
        a = random.randint(1,n-1)
        res = miller_rabin_test(n,a,m,k)
        if res!=1:
            break

    return res


def gcd(a,b):
    if b>a:
        a,b = b,a
    while(b!=0):
        c=a%b
        a=b
        b=c
    return a


def RSA_gen(lenth):
    import random

    if lenth == 256:
        lenth = 2**128
    elif lenth == 512:
        lenth = 2**256
    elif lenth == 1024:
        lenth = 2**512

    p = lenth
    q = lenth

    while 1:
        while is_prime(p)!=1:
            p = random.randint(lenth,lenth*2-1)

        while is_prime(q)!= 1 and p!=q:
            q = random.randint(lenth,lenth*2-1)

        n = p*q

        if(n>=lenth*lenth and n <= lenth*lenth*2-1):
            break
        else:
            p = random.randint(lenth,lenth*2-1)
            q = random.randint(lenth,lenth*2-1)


    pin = (p-1)*(q-1)



    e = 65537


    tempeVerse,temppinVerse = ext_gcd(e,pin)


    if(tempeVerse > 0):
        d = tempeVerse
    else:
        d = tempeVerse + pin


    return (n,e),(p,q,d)



def RSA_encrypt(message, pk):

    n,e = pk

    res = mod_exp(message,e,n)

    return res

def RSA_decrypt(ctmessage,sk):

    p,q,d = sk

    a = mod_exp(ctmessage,d,p)
    b = mod_exp(ctmessage,d,q)
    res=crt(p,q,a,b)

    return res

def RSA_test(key_len_list):
    key_len_list = [256,512,1024]
    idx = random.randint(0,2)
    print "crypted message legth : %d bit" %key_len_list[idx]
    pk,sk = RSA_gen(key_len_list[idx])

    print "n is : %d" %pk[0]
    print "e is : %d" %pk[1]

    print "p is : %d" %sk[0]
    print "q is : %d" %sk[1]
    print "d is : %d" %sk[2]

    num = random.randint(1,2**(key_len_list[idx]-1))

    print "\noriginal message => "
    print num

    ct = RSA_encrypt(num, pk)
    print "\nencrypted message => "
    print ct

    print "\ndecrypted message =>"
    print RSA_decrypt(ct,sk)

key_length_list = [256, 512, 1024]
RSA_test(key_length_list)
