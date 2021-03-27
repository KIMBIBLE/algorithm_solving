def solution(a, n, k):
    answer = 0
    for m in a:
        answer += int(k / m)
        k %= m

    return answer


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())

    res = solution(a[::-1], n, k)
    print(res)
