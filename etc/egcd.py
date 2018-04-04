def extended_gcd(a, b):
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    
    while r[-1] != 0:
        q = int(r[-2] / r[-1])
        r.append(r[-2] - q * r[-1])
        s.append(s[-2] - q * s[-1])
        t.append(t[-2] - q * t[-1])
    
    print 'gcd value : ' + str(r[-2])
    print 'x : ' + str(s[-2])
    print 'y : ' + str(t[-2])



extended_gcd(45, 78)
extended_gcd(666, 1428)
extended_gcd(1020, 10290)
extended_gcd(2 ** 20 + 4, 3 ** 10 + 5)
extended_gcd(2 ** 30 + 1, 3 ** 30 + 6)