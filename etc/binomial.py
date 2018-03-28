#!/usr/bin/python

global max
global d

def binomial(n, k):
    if k <= 0 or n == k:
        return 1
    if d[n][k] > 0:
        return d[n][k]

    d[n][k] = (binomial(n-1, k-1) + binomial(n-1, k))

    return d[n][k]


max = int(raw_input("input max value of n, k : "))
while True:
    d = [[0]*max for i in range(max)]
    n = int(raw_input("input n : "))
    for k in range(n+1):
        print "k=" + str(k) + " : " + str(binomial(n, k))