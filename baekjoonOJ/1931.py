def solution(n, m):
    answer = 1
    m.sort(key=lambda x: (x[1], x[0]))
    choice = m[0]
    for i in range(1, n):
        if choice[1] <= m[i][0]:
            answer += 1
            choice = m[i]

    return answer


if __name__ == '__main__':
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))

    res = solution(n, m)
    print(res)
