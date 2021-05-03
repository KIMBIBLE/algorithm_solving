"""
n이 백만이라 정렬 자체는 퀵소트 쓰면 1초 시간제한은 무난할 것 같음
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('{x} {y}'.format(x=self.x, y=self.y))


if __name__ == '__main__':
    N = int(readline())
    points = []
    for _ in range(N):
        x, y = map(int, readline().split())
        points.append(Point(x, y))
    
    sorted_points = sorted(points, key = lambda x: (x.x, x.y))
    for point in sorted_points:
        point.print()