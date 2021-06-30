"""
# Input Data 1 
7
1 3 5 7 9 11 13 15 17 19

# Output 1
4


# Input Data 2
7
1 3 5 6 9 11 13 15 17 19

# Output 2
Cannot find 7 in list
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)


if __name__ == '__main__':
    target = int(readline())
    array = list(map(int, readline().split()))

    result = binary_search(array, target, 0, len(array) - 1)
    if result == None:
        print('Cannot find {} in list'.format(target))
    else:
        print(result + 1)