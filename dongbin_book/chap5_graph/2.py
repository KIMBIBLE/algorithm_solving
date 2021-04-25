"""
4 <= N, M <= 200
O(5*N*M) <= 200000

INPUT SAMPLE
5 6
101010
111111
000001
111111
111111
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()
from collections import deque


class Graph:
    MONSTER_AREA = 0
    VALID_AREA = 1
    START_POS = -1

    def __init__(self):
        self.n, self.m = map(int, readline().split())
        self.matrix = [[Graph.MONSTER_AREA for _ in range(self.m + 2)]]
        for _ in range(self.n):
            data_feed = list(map(int, list(readline())))
            self.matrix.append([Graph.MONSTER_AREA] + data_feed + [Graph.MONSTER_AREA])
        
        self.matrix.append([Graph.MONSTER_AREA] * (self.m + 2))

    def bfs(self):
        movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((1, 1))
        self.matrix[1][1] = Graph.START_POS

        while queue:
            row, col = queue.popleft()
            if row == self.n and col == self.m:
                return self.matrix[row][col]

            for offset in movements:
                next_row = row + offset[0]
                next_col = col + offset[1]
                if self.matrix[next_row][next_col] == Graph.VALID_AREA:
                    queue.append((next_row, next_col))
                    if self.matrix[row][col] == Graph.START_POS:
                        self.matrix[next_row][next_col] = 2
                    else:
                        self.matrix[next_row][next_col] = self.matrix[row][col] + 1

    def show(self):
        for each in self.matrix:
            print(each)

if __name__ == '__main__':
    graph = Graph()
    #graph.show()
    print(graph.bfs())
    #graph.show()