"""
카드의 개수 N(3 ≤ N ≤ 100)
타겟 넘버: M(10 ≤ M ≤ 300,000)

n개중에 3개 선택: nC3
O(nC3) = O(min(n^3, n^(n-3)))

조합이지만 뽑는 갯수 자체가 3개로 고정되어 있어, 최악의 경우 시간 복잡도를 계산해보더라도
O(100C3) = O(min(100^3, 100^97)) = 1,000,000 정도가 나올 듯!
"""

import sys
from itertools import combinations

readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n, m = map(int, readline().split())
    nums = list(map(int, readline().split()))

    cases = combinations(nums, 3)

    diff = (-1, -1, -1) # INVALID STATE
    for case in cases:
        if (case[0] + case[1] + case[2]) > m:
            continue
        
        if (diff[0] + diff[1] + diff[2]) < (case[0] + case[1] + case[2]):
            diff = case

    #print(diff)
    print(diff[0] + diff[1] + diff[2])
