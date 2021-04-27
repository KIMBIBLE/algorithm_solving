"""
사람들은 1, 2, 3, …, n (1≤n≤100)의 연속된 번호로 각각 표시 -> 노드 수
엣지 수: n * (n - 1)
BFS 시간복잡도: O_worst(n + n ^2) = O(n^2) -> 최대 10000정도
"""

import sys, math
from collections import deque

readline = lambda: sys.stdin.readline().rstrip()

class Graph:
    NOT_VISITED = math.inf

    def __init__(self):
        self.n = int(readline()) # 노드 수
        self.start, self.end = map(int, readline().split())
        self.m = int(readline()) # 엣지 수

        self.adj = [[] for i in range(self.n + 1)]
        for _ in range(self.m):
            u, v = map(int, readline().split())
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.visited = [Graph.NOT_VISITED] * (self.n + 1)


    def bfs(self):
        queue = deque([self.start])
        self.visited[self.start] = 0

        while queue:
            cur_node = queue.popleft()
            
            if cur_node == self.end:
                break
            
            for nxt_node in self.adj[cur_node]:
                if self.visited[nxt_node] == Graph.NOT_VISITED:
                    queue.append(nxt_node)
                    self.visited[nxt_node] = self.visited[cur_node] + 1
                
        if self.visited[self.end] == math.inf:
            return -1
        else:
            return self.visited[self.end]

    def show(self):
        for idx, v in enumerate(self.adj):
            print(idx, '-> ', v)

        print(self.visited)

if __name__ == '__main__':
    g = Graph()
    #g.show()
    print(g.bfs())
    #g.show()