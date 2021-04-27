import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    while True:
        a, b = map(int, readline().split())
        if a == b == 0:
            break
    
        print(a + b)