def solution(x):
    answer = 0
    _x = 1000 - x
    collections = [500, 100, 50, 10, 5, 1]
    for unit in collections:
        answer += _x // unit
        _x %= unit

    return answer

if __name__ == '__main__':
    res = solution(int(input()))
    print(res)