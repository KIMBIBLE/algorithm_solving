import random

def counting_sort(data):
    sorted_data = []
    count = [0] * (max(data) + 1)

    for i in range(len(data)):
        count[data[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            #print(i, end=' ')
            sorted_data.append(i)

    return sorted_data

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = counting_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# before: [7, 3, 5, 7, 5, 6, 3, 10, 4, 8]
# after:  [3, 3, 4, 5, 5, 6, 7, 7, 8, 10]