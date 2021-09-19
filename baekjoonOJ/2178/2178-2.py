import sys
readline = lambda: sys.stdin.readline().rstrip()
from collections import deque

class Graph:
    UNAVAILABLE    = 0
    AVAILABLE       = 1
    START_LEVEL     = -1

    def __init__(self):
        self.n, self.m = map(int, readline().split()) # n행, m열

        # n+2 행, m+2 열 배열 생성: access 불가능한 경계선 추가
        self.matrix = [[Graph.UNAVAILABLE for _ in range(self.m + 2)]]
        for _ in range(self.n):
            data = list(map(int, list(readline())))
            self.matrix.append([Graph.UNAVAILABLE] + data[:] + [Graph.UNAVAILABLE])

        self.matrix.append([Graph.UNAVAILABLE for _ in range(self.m + 2)])

    
    def bfs(self):
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # d_row, d_col: 상하좌우 이동
        queue = deque()
        queue.append((1, 1)) # start pos(row, col)
        self.matrix[1][1] = Graph.START_LEVEL

        while queue:
            cur_row, cur_col = queue.popleft()
            if cur_row == self.n and cur_col == self.m:
                return self.matrix[cur_row][cur_col] # 도착
            
            for offset in move:
                next_row = cur_row + offset[0]
                next_col = cur_col + offset[1]
                if self.matrix[next_row][next_col] == Graph.AVAILABLE:
                    queue.append((next_row, next_col))

                    if self.matrix[cur_row][cur_col] == Graph.START_LEVEL:
                        self.matrix[next_row][next_col] = 2
                    else:
                        self.matrix[next_row][next_col] = self.matrix[cur_row][cur_col] + 1

    
    def show(self):
        for line in self.matrix:
            for item in line:
                print('{:4d}'.format(item), end='')
            print()



if __name__ == '__main__':
    graph = Graph()
    graph.show()
    print(graph.bfs())
    graph.show()
