def solution(n):
    for y in range(n // 5, -1, -1):
        for x in range(n // 3 + 1):
            if 3 * x + 5 * y == n:
                return x+y

    return -1


if __name__ == '__main__':
    res = solution(int(input()))
    print(res)