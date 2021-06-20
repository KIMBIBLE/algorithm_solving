"""
[입력]
5 3 (1<= N, K <= 100,000)
1 2 3 4 5 (각각의 원소는 10,000,000 보다 작은 자연수) 
5 5 6 5 5 

[분석]
배열 A의 원소의 합을 최대로, K번 바꿔치기

0 1 2 3 4
------------
1 2 3 4 5 -> 오름차순
6 5 5 5 5 -> 내림차순
      K
"""

import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    N, K = map(int, readline().split())
    arr1 = list(map(int, readline().split()))
    arr2 = list(map(int, readline().split()))

    arr1.sort()
    arr2.sort(reverse = True)

    sum = 0
    for idx in range(N):
        if idx < K:
            sum += arr2[idx]

        else:
            sum += arr1[idx]

    print(sum)