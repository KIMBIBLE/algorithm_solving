import sys
readline = lambda: sys.stdin.readline()

def solution(n, dice_nums):
    res = 0

    if n == 1:
        dice_nums.sort()
        dice_nums.pop()
        for item in dice_nums:
            res += item
            
        return res
    
    minvals = [min(dice_nums[0], dice_nums[5]), min(dice_nums[1], dice_nums[4]), min(dice_nums[2], dice_nums[3])]
    minvals.sort()

    dim1 = minvals[0]
    dim2 = minvals[0] + minvals[1]
    dim3 = minvals[0] + minvals[1] + minvals[2]


    dims_cnt = [4 * (n - 2) * (n - 1) + (n - 2) ** 2, 4 * (n - 1) + 4 * (n - 2), 4]
    res = dim1 * dims_cnt[0] + dim2 * dims_cnt[1] + dim3 * dims_cnt[2]

    return res


if __name__ == '__main__':
    n = int(readline())
    dice_nums = list(map(int, readline().split()))

    print(solution(n, dice_nums))

