import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    n, k = map(int, readline().split())
    step = 0
    while n != 1:
        step += 1
        if n % k == 0:
            n //= k
        else:
            n -= 1

    print(step)