"""
10000 이하 자연수 2개(a, b) -> 최대공약수, 최소공배수
최대공약수 <- GCD(a, b)
최소공배수 <- a * b / GCD(a, b)

gcd: 유클리드 알고리즘
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a

    else:
        if b > a:
            a, b = b, a
        
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    a, b = map(int, readline().split())
    print(gcd(a, b))
    print(lcm(a, b))