import sys
from collections import deque
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n = int(readline())
    d = deque([x for x in range(1, n + 1)])
    while len(d) != 1:
        d.popleft()
        num = d.popleft()
        d.append(num)

    print(*d)