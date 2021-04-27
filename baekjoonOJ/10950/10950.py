import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n = int(readline())
    for _ in range(n):
        a, b = map(int, readline().split())
        print(a + b)