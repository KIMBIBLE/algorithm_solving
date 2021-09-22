class Graph:
    def __init__(self, V):
        self.V = V
        self.matrix = [[False for _ in range(self.V + 1)] for _ in range(self.V + 1)]
        self.visited = [False for _ in range(self.V + 1)]

    def addEdge(self, v, w):
        self.matrix[v][w] = True
        self.matrix[w][v] = True

    def dfs(self, s = 1):
        self.visited[s] = True
        print(s, end=' ')

        for idx in range(self.V + 1):
            if self.matrix[s][idx] == True and self.visited[idx] == False:
                self.dfs(idx)

g = Graph(8)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 8)
g.addEdge(2, 7)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(6, 7)
g.addEdge(7, 8)

g.dfs() # 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5