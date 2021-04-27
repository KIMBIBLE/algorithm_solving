"""
M(행) * N(열) 크기 모눈종이(1<= M, N <= 100), 눈금간격이 1이라 최소값 1로 잡음
K개의 직사각형(1 <= K <= 100)

answer1: K개의 직사각형 내부를 제외한 나머지 부분이 몇 부분으로 나누어지는지
- 배열의 모든 원소를 대상으로 dfs/bfs 수행하며, 연결 요소의 갯수 탐색
- 초기 반복에서 배열의 원소가 방문 안한 곳이면 카운터 증가하고 dfs/bfs 수행
- 직사각형에 해당되는 곳 -> INVALID, 없는곳 VALID

answer2: 분리된 각 영역의 넓이가 얼마인지?
- 초기 반복에서 한번 dfs/bfs를 수행하면 몇개의 원소를 탐색하는지

그래프 구현 시 연결리스트 방식보다 배열 방식이 좌표 표현하기에 직관적일 듯
2차원 배열에 대한 DFS/BFS의 시간복잡도: O(M*N * 4) <= 40000

좌표(x, y) 기준으로 입력값이 주어지기 때문에 좌표-> 행렬 변환식 구성해야 함
src_x, src_y, dst_x, dst_y

src_y <= i < dst_y
src_x <= j < dst_x

"""

import sys, math
readline = lambda: sys.stdin.readline().rstrip()

class Graph:
    VALID = 0
    INVALID = math.inf
    VISITED = 1

    def __init__(self):
        self.M, self.N, self.K = map(int, readline().split())
        self.matrix = [[Graph.VALID for _ in range(self.N)] for _ in range(self.M)]
        for _ in range(self.K):
            src_x, src_y, dst_x, dst_y = map(int, readline().split())
            for i in range(src_y, dst_y):
                for j in range(src_x, dst_x):
                    self.matrix[i][j] = Graph.INVALID

    def show(self):
        for each in self.matrix:
            for x in each:
                print(str(x).ljust(5), end=' ')
            print()

    def dfs(self, node):
        movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [node]
        cnt = 0

        while stack:
            cur_node = stack.pop()
            row = cur_node[0]
            col = cur_node[1]

            if self.matrix[row][col] == Graph.VALID:
                self.matrix[row][col] = Graph.VISITED
                cnt += 1

            for offset in movements:
                nxt_row = row + offset[0]
                nxt_col = col + offset[1]

                # oob check
                if nxt_row < 0 or nxt_row >= self.M:
                    continue
                
                # oob check
                if nxt_col < 0 or nxt_col >= self.N:
                    continue

                if self.matrix[nxt_row][nxt_col] == Graph.VALID:
                    stack.append((nxt_row, nxt_col))

        return cnt


    def run(self):
        secter_cnt = 0
        secter_size = []

        for i in range(self.M):
            for j in range(self.N):
                if self.matrix[i][j] == Graph.VALID:
                    secter_cnt += 1
                    x = self.dfs((i, j))
                    secter_size.append(x)

        print(secter_cnt)
        for x in sorted(secter_size):
            print(x, end=' ')


if __name__ == '__main__':
    g = Graph()
    #g.show()
    g.run()
    #g.show()
