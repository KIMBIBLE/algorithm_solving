import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    n, m, k = map(int, readline().split())
    nums = list(map(int, readline().split()))
    nums.sort(reverse=True)

    res = 0
    counter = 0
    first = nums[0]
    second = nums[1]
    for _ in range(m):
        if counter == k:
            res += second
            counter = 0
        else:
            res += first
            counter += 1
    
    print(res)
