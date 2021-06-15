import random

def selection_sort(data_to_sort):
    for i in range(len(data_to_sort) - 1):
        min_idx = i
        for j in range(i + 1, len(data_to_sort)):
            if data_to_sort[min_idx] > data_to_sort[j]:
                min_idx = j
        data_to_sort[i], data_to_sort[min_idx] = data_to_sort[min_idx], data_to_sort[i]

    return data_to_sort

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))