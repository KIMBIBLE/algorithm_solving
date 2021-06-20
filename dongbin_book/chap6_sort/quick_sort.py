import random

def quicksort(data, start, end):
    if start >= end: # 원소가 1개인 경우 재귀 종료
        return
    
    pivot = start       # 첫번 째 원소의 인덱스를 피벗으로 설정

    left = pivot + 1    # 피벗보다 큰 값을 찾기 위한 인덱스의 시작 값을 
                        # 피벗의 바로 우측 값으로 설정

    right = end         # 피벗보다 작은 값을 찾기 위한 인덱스의 시작 값을
                        # 리스트의 가장 우측 인덱스로 설정

    # left와 right이 엇갈릴 때까지, 피벗을 기준으로 좌측과 우측 데이터의 위치 교환을 반복
    while left <= right:
        # 피벗보다 큰 데이터의 인덱스 찾기
        while left <= end and data[left] <= data[pivot]:
            left += 1
        
        # 피벗보다 작은 데이터의 인덱스 찾기
        while start < right and data[right] >= data[pivot]:
            right -= 1

        # left와 right이 엇갈린 경우
        if left >= right:
            # 작은 데이터와 피벗의 위치를 swap
            data[pivot], data[right] = data[right], data[pivot]

        # left와 right이 엇갈리지 않은 경우
        else:
            # 작은 데이터와 큰 데이터의 위치를 swap
            data[right], data[left] = data[left], data[right]

    # 분할 완료
    quicksort(data, start, right - 1)    # 피벗의 좌측 데이터들을 대상으로 정렬 수행
    quicksort(data, left, end)      # 피벗의 우측 데이터들을 대상으로 정렬 수행



data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(data))
quicksort(data, 0, len(data) - 1)
print('after:  {}'.format(data))

# before: [7, 3, 0, 5, 8, 6, 1, 10, 7, 8]
# after:  [0, 1, 3, 5, 6, 7, 7, 8, 8, 10]