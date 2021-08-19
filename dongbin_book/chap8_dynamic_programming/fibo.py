"""
1 1 2 3 5 8 13 21

f(5) 
    f(4)
        f(3)
            f(2)
            f(1) 
        f(2) 
    f(3) 
        f(2)
        f(1)
"""

import sys
sys.setrecursionlimit(4000)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    return fibo(x - 1) + fibo(x - 2)

def print_fibo_sequence(x):
    print("f({})".format(x), end = ' ')
    
    if x == 1 or x == 2:
        return 1
    
    return print_fibo_sequence(x - 1) + print_fibo_sequence(x - 2)

if __name__ == '__main__':
    target = int(input())
    print('\n{}'.format(print_fibo_sequence(target)))