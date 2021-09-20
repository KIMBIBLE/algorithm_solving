from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [ [] for _ in range(V + 1)] #adjacency list
        self.visited = [False] * (V + 1)

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def bfs(self, s = 1):
        queue = deque([s])
        self.visited[s] = True

        while queue:
            cur_node = queue.popleft()
            print(cur_node, end = ' ') # 노드 출력

            for linked_node in self.adj[cur_node]:
                if self.visited[linked_node] == False:
                    queue.append(linked_node)
                    self.visited[linked_node] = True


    def showGraph(self):
        for cur_node, cur_node_info in enumerate(self.adj):
            print(cur_node, end=': ')
            for linked_node in cur_node_info:
                print(linked_node, end = ' ')
            print()



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

g.showGraph()

g.bfs() # 1 2 3 8 7 4 5 6