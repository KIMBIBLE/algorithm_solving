"""
1 1 2 3 5 8 13 21
"""

import sys
sys.setrecursionlimit(4000)

d = [0] * 10000

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] == 0:
        d[x] = fibo(x - 1) + fibo(x - 2)
    
    return d[x]

def print_fibo_dp_sequence(x):
    if x == 1 or x == 2:
        print('f({})'.format(x), end = ' ')
        return 1

    if d[x] == 0:
        print('f({})'.format(x), end = ' ')
        d[x] = print_fibo_dp_sequence(x - 1) + print_fibo_dp_sequence(x - 2)
    
    return d[x]
    
if __name__ == '__main__':
    print(print_fibo_dp_sequence(int(input())))