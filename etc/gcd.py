def gcd(a,b):
    if b>a:
        a,b = b,a
    while(b!=0):
        c=a%b
        a=b
        b=c
    return a
 
def extended_gcd(a,b):
    s0=1
    s1=0
    t0=0
    t1=1
    i=0
    cnt=0
    check=0
    d=[]
    if b>a:
        a,b = b,a
        check=1
    while(b!=0):
        c=a%b
        d.append(a//b)
        a=b
        b=c
        if i>=1:
            s2=(-1)*d[cnt]*s1+s0
            s0=s1
            s1=s2
            t2=(-1)*d[cnt]*t1+t0
            t0=t1
            t1=t2
            cnt+=1
        i+=1
    if check==1:
        return a,t2,s2
    
    return a,s2,t2

print gcd(45, 75)
print extended_gcd(45, 75)
print gcd(666, 1414)
print extended_gcd(666, 1414)
print gcd(102, 222)
print extended_gcd(102, 222)