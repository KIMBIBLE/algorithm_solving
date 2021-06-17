import sys
sys.setrecursionlimit(2000)
readline = lambda: sys.stdin.readline().rstrip()

def fibo(n, x, memo):
    if n == 0:
        x[n] += 1
        #print("0", end='')
        return 0

    elif n == 1:
        x[n] += 1
        #print("1", end='')
        return 1

    else:
        return fibo(n-1, x, memo) + fibo(n-2, x, memo)


if __name__ == '__main__':
    tc = int(readline())
    for _ in range(tc):
        n = int(readline())
        x = [0, 0]
        memo = [0] * (n + 1)
        fibo(n, x, memo)
        print('\n{} {}'.format(x[0], x[1]))
