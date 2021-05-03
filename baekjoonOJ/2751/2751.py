"""
1,000,000(100만개) 정렬
시간제한 2초이고, 정렬 시 추가적인 고려사항이 없어 파이썬 내장인 퀵소트로 충분할듯

O_worst(NlgN) = 1,000,000 * 7
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(readline())
    nums = []
    for _ in range(N):
        nums.append(int(readline()))

    nums.sort()
    for num in nums:
        print(num)