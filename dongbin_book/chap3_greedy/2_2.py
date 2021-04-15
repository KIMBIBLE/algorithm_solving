import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    n, m, k = map(int, readline().split())
    nums = list(map(int, readline().split()))
    nums.sort() # O(nlgn)
    a = nums[-1]
    b = nums[-2]

    if a == b:
        res = a * m
    else:
        res = a * m - (a - b) * ((m - 1) // k)

    print(res)