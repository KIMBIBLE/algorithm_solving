def solution(n, p):
    answer = 0
    p.sort()
    for i in range(n):
        answer += p[i] * (n - i)

    return answer


if __name__ == '__main__':
    n = int(input())
    p = [int(x) for x in input().split()]

    res = solution(n, p)
    print(res)
