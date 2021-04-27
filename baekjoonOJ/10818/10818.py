import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n = int(readline())
    nums = list(map(int, readline().split()))
    print(min(nums), end=' ')
    print(max(nums))