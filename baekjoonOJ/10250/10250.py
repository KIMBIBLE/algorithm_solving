import sys
readline = lambda: sys.stdin.readline().rstrip()

def solution(H, W, N):
    h = N % H
    if h == 0:
        h = H
    
    w = ((N - h) // H) + 1

    print(h)

    print(str(h) + str(w).rjust(2, '0'))

if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        H, W, N = map(int, readline().split())
        solution(H, W, N)
