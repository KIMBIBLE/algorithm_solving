# 인덱스 찾기 문제

import sys, re
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    expr = readline()
    operators = ['+'] + re.compile('\+|-').findall(expr)
    nums = list(map(int, re.compile('[0-9]+').findall(expr)))

    res = 0

    try:
        idx = operators.index('-')
        for i in range(idx):
            res += nums[i]

        for j in range(idx, len(operators)):
            res -= nums[j]

    except:
        res = sum(nums)

    print(res)
        

