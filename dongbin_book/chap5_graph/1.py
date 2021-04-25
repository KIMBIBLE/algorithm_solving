# 1 <= N, M <= 1000
# 시간제한: 1초 
# 5 <= O(N * M + 4 * N * M) = O(5 * N * M) <= 5000000

"""
IMPUT SAMPLE
15 14
00000111100000
11111101111110 
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

VAILD_AREA = 0
INVALID_AREA = 1
VISITED_AREA = 2

class Graph:
    def __init__(self, N, M):
        self.n = N # row
        self.m = M # col

        # N행 M열 -> (N + 2)행 (M + 2)열 with dummy
        self.matrix = [[INVALID_AREA for _ in range(M + 2)]]
        for _ in range(N):
            feed = list(map(int, list(readline())))
            self.matrix.append([INVALID_AREA] + feed + [INVALID_AREA] )
        self.matrix.append([INVALID_AREA for _ in range(M + 2)])


    def dfs(self, node):
        row = node[0]
        col = node[1]
        self.matrix[row][col] = VISITED_AREA

        movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for offset in movement:
            next_row = row + offset[0]
            next_col = col + offset[1]

            if self.matrix[next_row][next_col] == VAILD_AREA:
                self.dfs((next_row, next_col))


    def show(self):
        for each in self.matrix:
            print(each)


    def run(self):
        self.cnt = 0

        for i in range(1, self.n + 1): # 1 ~ n
            for j in range(1, self.m + 1): # 1 ~ m+1
                if self.matrix[i][j] == VAILD_AREA:
                    self.cnt += 1
                    self.dfs((i, j))

        return self.cnt


if __name__ == '__main__':
    N, M = map(int, readline().split())
    graph = Graph(N, M)
    #graph.show()
    print(graph.run())
    #graph.show()

