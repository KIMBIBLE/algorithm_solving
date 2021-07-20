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

if __name__ == "__main__":
    N = int(readline())
    data = list(map(int, readline().split()))
    M = int(readline())
    targets = list(map(int, readline().split()))
    data.sort() # O(N log N)

    for target in targets: # O(M)
        if binary_search(data, target, 0, len(data) - 1) is not None: # O(log N)
            print("yes", end = ' ')
        else:
            print("no", end = ' ')
