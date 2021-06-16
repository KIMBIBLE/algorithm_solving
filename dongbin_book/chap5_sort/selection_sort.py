import random

def selection_sort(data_to_sort):
    for i in range(1, len(data_to_sort)):
        for j in range(i, 0, -1):
            if data_to_sort[j - 1] > data_to_sort[j]:
                data_to_sort[j - 1], data_to_sort[j] = data_to_sort[j], data_to_sort[j -1]
            
            else:
                break
    
    return data_to_sort

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))