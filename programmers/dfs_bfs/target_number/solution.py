# 시간초과 (Exhaustive Search: Brute Force)
def solution_2(numbers, target):
    answer = 0
    import itertools
    operators = [1] * (len(numbers) + 1)
    operators[0] = 0    # dummy value

    for i in range(len(operators)):
        operators[i] = -1
        p = set(itertools.permutations(operators[1:]))
        for ops in p:
            num = 0
            for j in range(len(ops)):
                num += ops[j] * numbers[j]

            if num == target:
                answer += 1

    return answer


# 시간초과 (Exhaustive Search: Brute Force)
def solution_1(numbers, target):
    answer = 0
    import itertools
    operators = list('_' + '+' * len(numbers)) # ' ' is dummy. it'll be stripped in later

    for i in range(len(operators)):
        operators[i] = '-'
        p = set(itertools.permutations(operators[1:], len(operators) - 1 ))
        for ops in p:
            # ops looks like: ('+', '+', '+', '+', '-')
            num = 0
            for j in range(len(ops)):
                if ops[j] == '+':
                    num += numbers[j]

                else:
                    num -= numbers[j]

            if num == target:
                answer += 1

    return answer


if __name__ == '__main__':
    import sys
    readline = lambda: sys.stdin.readline()
    numbers = list(map(int, readline().split()))
    target = int(readline())
    print(solution(numbers, target))
