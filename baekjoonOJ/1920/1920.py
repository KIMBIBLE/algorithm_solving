"""
시간제한: 2초
메모리제한: 128MB: 128,000,000

자연수 N(1 ≤ N ≤ 100,000), N개의 정수 A[1], A[2], …, A[N]
M(1 ≤ M ≤ 100,000), M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지
-2^31 <= 각각의 수 <= 2^31


* 순차적으로 탐색하는 방법
시간복잡도: 1 <= O(N * M) <= 10,000,000,000

* 정수 범위를 배열로 표현
시간복잡도: 1 <= O(N + M) <= 100,000
공간복잡도: 2147483648 + 1 + 2147483648 (바이트 표현은 안됨)

* 모든 N에 대하여 해싱하여 저장하는 방법

"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(readline())
    A = list(map(int, readline().split()))

    M = int(readline())

    target = list(map(int, readline().split()))
    m = {num:True for num in A}
    
    for t in target:
        try:
            m[t]
            print(1)

        except:
            print(0)
