def mod_exp(a,e,m):
    tmp=a
    c=[]
    total=1
    length=0
    j=0
    i=1
    while 1:
        if(e<2):
            c.append(e)
            break;
        c.append(e%2)
        e=e//2
        
    length=len(c)
    
    for j in range(0,length):
        if c[j]==1:
            total=total*tmp
            total=total%m
        tmp=tmp**2
        tmp=tmp%m
    return total

def crt(p,q,a,b):
    m1=q
    m2=p
    y1=1
    y2=1

    while(y1*m1%p!=1):
        y1=y1+1

    while(y2*m2%q!=1):
        y2=y2+1

    print(y2*m2)
        
    return ((a*m1*y1)+(b*m2*y2))%(p*q)

def crt_list(primes, values):
    a=[]
    m=[]
    y=[]
    x=1
    g=1
    result=0
    
    for i in range(0,len(primes)):
                   g=g*primes[i]
                   
    for i in range(0,len(primes)):
                   a.append(values[i]%primes[i])
                   m.append(g//primes[i])
                   while(1):
                       if(x*m[i]%primes[i]==1):
                           y.append(x%primes[i])
                           break
                       x=x+1
                       
    for i in range(0,len(primes)):
                   result+=a[i]*m[i]*y[i]%g
                   
    return result%g

print mod_exp(3, 12345, 97)
print mod_exp(3, 123456789012345, 976)
print crt(10, 21, 1, 2)
print crt(257, 293, 11, 13)
print crt_list([10, 21, 29], [1, 2, 3])
print crt_list([257, 293, 337], [11, 13, 31])