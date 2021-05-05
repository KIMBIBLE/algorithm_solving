"""
시간제한: 1초, 메모리 제한: 256MB

점의 개수: N (1 ≤ N ≤ 100,000)
i번점의 위치 xi와 yi (-100,000 ≤ xi, yi ≤ 100,000) 
좌표는 항상 정수, 위치 같은 경우 없음
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("{x} {y}".format(x=self.x, y=self.y))

if __name__ == '__main__':
    N = int(readline())
    points = []
    for _ in range(N):
        x, y = map(int, readline().split())
        p = Point(x, y)
        points.append(p)
    
    sorted_points = sorted(points, key=lambda p: (p.y, p.x))
    for point in sorted_points:
        point.print()
