"""
M*N 크기 보드(8 <= M, N <= 50)
BLACK
WHITE
8*8 크기

맨 위칸이 흰색 or 검은색

42 * 42 * 8 * 8 * 2
"""

import sys, math
readline = lambda: sys.stdin.readline().rstrip()

BLACK = 'B'
WHITE = 'W'

def showArr(arr):
    for line in arr:
        print(line)

def draw(arr, i, j, color):
    cnt = 0

    for row in range(i, i + 8):
        for col in range(j, j + 8):
            if (row + col) % 2 == 0:
                if arr[row][col] != color:
                    cnt += 1

            else:
                if arr[row][col] == color:
                    cnt += 1

    return cnt

if __name__ == "__main__":
    m, n = map(int, readline().split())
    arr = []
    for i in range(m):
        line = list(readline())
        arr.append(line)

    #showArr(arr)

    min_val = math.inf
    for i in range(m - 7):
        for j in range(n - 7):
            cnt = draw(arr, i, j, BLACK)
            #print(cnt)
            if cnt < min_val:
                min_val = cnt

            cnt = draw(arr, i, j, WHITE)
            #print(cnt)
            if cnt < min_val:
                min_val = cnt

    print(min_val)

