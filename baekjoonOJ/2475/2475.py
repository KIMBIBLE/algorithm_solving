import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    nums = list(map(int, readline().split()))
    res = 0
    for num in nums:
        res += num ** 2

    print(res % 10)