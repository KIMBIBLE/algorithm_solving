#!/usr/bin/python

def f(n):
    if n <= 1:
        return 1
    return n*f(n-1) 

while True:
    n = int(raw_input("input num (0 is exit) : "))
    if n == 0:
        exit()

    print f(n)