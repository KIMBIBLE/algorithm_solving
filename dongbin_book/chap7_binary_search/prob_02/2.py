import sys

readline = lambda: sys.stdin.readline().rstrip()

def binary_search(array, M):
    start = 0
    end = max(array)

    result = 0
    while start <= end:
        H = (start + end) // 2
        total = 0
        for x in array:
            if x > H:
                total += x - H

        if total < M:       # 손님이 요청한 떡의 길이 조건을 만족하지 않는 경우
            end = H - 1

        else:               # 손님이 요청한 떡의 길이 조건을 만족하는 경우
            result = H      # 결과 저장
            start = H + 1   # 탐색 수행

    return result

if __name__ == "__main__":
    N, M = map(int, readline().split())
    array = list(map(int, readline().split()))

    result = binary_search(array, M)
    print(result)