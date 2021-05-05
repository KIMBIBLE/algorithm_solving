"""
시간 제한: 3초
메모리 제한: 8MB

N(1 ≤ N ≤ 10,000,000)개의 수 정렬
수(1<= x <= 10,000인 자연수)

O(nlgn): 80,000,000 (8천만 정도)
시간 제한이 3초니 3억정도까지 연산이 가능하니 O(nlgn)을 사용하면 될 듯.

이때 각각의 수가 10,000 미만이니 파이썬 리스트로 표현하면 87,61 Byte = 0.087616 MB로 메모리 제한이 안 걸림
또한 입력에서 중복 허용하니까 카운트 정렬 쓰면 O(1)으로 해결 가능할 듯

"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(readline())
    num_count = [0 for _ in range(10001)]
    for _ in range(N):
        x = int(readline())
        num_count[x] += 1

    for idx, n in enumerate(num_count):
        for _ in range(n):
            print(idx)
    