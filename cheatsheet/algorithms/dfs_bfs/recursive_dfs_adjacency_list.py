class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V + 1)]
        self.visited = [False for _ in range(self.V + 1)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def dfs(self, s = 1):
        self.visited[s] = True
        print(s, end=' ')

        for node in self.adj[s]:
            if self.visited[node] == False:
                self.dfs(node)

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