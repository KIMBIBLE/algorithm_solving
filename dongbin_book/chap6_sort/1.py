"""
Input
3
15
27
12

Output
27 15 12
"""
import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    N = int(readline())
    arr = [0] * N
    for idx in range(N):
        arr[idx] = int(readline()) 

    arr.sort(reverse = True)
    for each in arr:
        print(each, end = ' ')


