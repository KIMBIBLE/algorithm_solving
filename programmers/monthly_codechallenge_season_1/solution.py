def solution(numbers):
    answer = []
    res = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                res.add(numbers[i] + numbers[j])

    answer = list(res)
    answer.sort()

    return answer

if __name__ == '__main__':
    import sys
    readline = lambda: sys.stdin.readline()
    numbers = list(map(int, readline().split()))
    print(solution(numbers))