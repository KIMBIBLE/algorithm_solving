import random

def insertion_sort(data):
    for i in range(1, len(data)):
        # 삽입할 데이터를 한 칸씩 왼쪽으로 이동하며, 크기 비교 
        for j in range(i, 0, -1):
            # 저산보다 큰 데이터를 만나면 swap
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j -1]
            
            else: # 자신보다 작은 데이터를 만나면 해당 위치에서 정지
                break

    return data

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = insertion_sort(unsorted_data)
print('after:  {}'.format(sorted_data))