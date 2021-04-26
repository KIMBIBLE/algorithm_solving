"""
1 <= N(세로:행), M(가로:열) <= 100
1 <= K(음식물 쓰레기 갯수) <= 10,000
O(50000)

시간제한: 2초 -> 2억회 정도의 연산
그래프 탐색에 대한 비용: O(V^2) -> O_worst(100,000,000): 1억정도
"""
import sys, math
sys.setrecursionlimit(10000)
readline = lambda: sys.stdin.readline().rstrip()

class Graph:
    VALID = 0
    INVALID = math.inf
    VISITED = -1

    def __init__(self):
        self.n, self.m, self.k = map(int, readline().split())
        self.matrix = [[Graph.INVALID for _ in range(self.m + 2)] for _ in range(self.n + 2)]
        for _ in range(self.k):
            u, v = map(int, readline().split())
            self.matrix[u][v] = Graph.VALID


    def show(self):
        for each in self.matrix:
            print(each)
        print()
        

    def dfs(self, node):
        row = node[0]
        col = node[1]
        cnt = 1
        self.matrix[row][col] = Graph.VISITED

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for offset in movements:
            nxt_row = row + offset[0]
            nxt_col = col + offset[1]
            
            if self.matrix[nxt_row][nxt_col] == Graph.VALID:
                cnt += self.dfs((nxt_row, nxt_col))
        
        return cnt


    def run(self):
        max_val = 0

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.matrix[i][j] == Graph.VALID:
                    max_val = max(self.dfs((i, j)), max_val)
        
        print(max_val)



if __name__ == '__main__':
    g = Graph()
    #g.show()
    g.run()
    #g.show()
    


        

