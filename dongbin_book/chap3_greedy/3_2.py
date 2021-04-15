import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    n, m = map(int, readline().split())
    cards = [[0] * m for _ in range(n)]
    for i in range(n):
        nums = list(map(int, readline().split()))
        for j, num in enumerate(nums):
            cards[i][j] = num

    """
    O(n^2)
    """
    maxval = 0
    for row in cards: # O(n)
        row_min = min(row) # O(n)
        maxval = max(maxval, row_min)
    
    print(maxval)