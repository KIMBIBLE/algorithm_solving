"""
max: 1000000000 - 1
min: 1000000
"""

import sys, collections
read = lambda: sys.stdin.read().rstrip()


if __name__ == "__main__":
    a, b, c = map(int, read().split())
    val = str(a * b * c)
    numeric = [0] * 10
    for x in val:
        numeric[ord(x) - ord('0')] += 1

    for n in numeric:
        print(n)
    