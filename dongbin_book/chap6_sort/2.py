"""
1<=N<=100,000

입력
2
홍길동 95
이순신 77

출력: 성적이 낮은 순
이순신 홍길동
"""

import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    N = int(readline())
    arr = []

    for _ in range(N):
        name, score = readline().split()
        arr.append((name, int(score)))

    arr.sort(key = lambda x: x[1])
    for item in arr:
        print(item[0], end = ' ')