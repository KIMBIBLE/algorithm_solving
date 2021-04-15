"""
O(n^2 * mlgm)

최솟값이나 최댓값만 찾는 문제에서는 정렬 알고리즘을 사용하면
구현하기는 편하긴 하지만 성능 하락이 있음.

따라서 그냥 min/max 값 구하는 방식이 효율적
"""

import sys
readline = lambda: sys.stdin.readline()

MIN_NUM = 0

if __name__ == '__main__':
    n, m = map(int, readline().split())
    cards = [[0] * m for _ in range(n)]
    for i in range(n):
        nums = list(map(int, readline().split()))
        for j, num in enumerate(nums):
            cards[i][j] = num

    for row in cards: # O(n * mlgm)
        row.sort() 
    
    maxval = MIN_NUM
    for i in range(n): # O(n)
        if cards[i][0] > maxval:
            maxval = cards[i][0]

    print(maxval)