import random

def selection_sort(data):
    # 선택된 최솟값과 swap할 대상의 인덱스
    for i in range(len(data)):
        # 아직 정렬되지 않은 데이터에 대해 최솟값 찾기 수행
        min_idx = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))