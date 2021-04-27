import sys
read = lambda: sys.stdin.read().rstrip()

if __name__ == "__main__":
    max_val = -1
    max_idx = 0
    nums = list(map(int, read().split()))

    for num in nums:
        if num >= max_val:
            max_val = num

    print(max_val)
    print(nums.index(max_val) + 1)