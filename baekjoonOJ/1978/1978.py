"""
시간제한: 2초

1~1000 까지 수에 대해 소수 판별
1: 소수X

1과 자기자신을 제외한 수로 나누기 반복
2   3   4   5 + ....   1000
0 + 1 + 2 + 3 + .... +  998 = (998 * 999) / 2 = 498501 

O(1000) = (998 * 999) / 2 = 498501 
O(N) = (N^2) / 2 

시간제한 2초에 1000까지 수 까지만 소수 판별하는것이기 때문에 위 방법으로도 충분할듯
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

def is_prime(num):
    if num == 1:
        return False

    if num == 2:
        return True

    for divider in range(2, num - 1):
        if num % divider == 0:
            return False

    return True

    
if __name__ == "__main__":
    n = int(readline())
    target = list(map(int, readline().split()))
    cnt = 0

    for t in target:
        if is_prime(t):
            cnt += 1

    print(cnt)

