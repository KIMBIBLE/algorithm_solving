"""
20*8*1000
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T = int(readline())
    for _ in range(T):
        R, S = readline().split()
        R = int(R)
        res = ""
        for x in S:
            res += x * R
        
        print(res)