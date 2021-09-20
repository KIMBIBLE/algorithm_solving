from collections import deque


class Graph:
    CONNECTED = 1

    def __init__(self, V):
        self.V = V # vertex 갯수
        self.matrix = [ [0 for _ in range(V + 2)] for _ in range(V + 2)]
        self.visited = [False] * (V + 1)

    def addEdge(self, v, w):
        self.matrix[v][w] = Graph.CONNECTED
        self.matrix[w][v] = Graph.CONNECTED


    def bfs(self, s = 1):
        queue = deque([s])
        self.visited[s] = True

        while queue:
            cur_node = queue.popleft()
            print(cur_node, end = ' ') # 노드 출력

            for node, item in enumerate(self.matrix[cur_node]):
                if item == Graph.CONNECTED and self.visited[node] == False:
                    queue.append(node)
                    self.visited[node] = True


    def showGraph(self):
        print(' ' * 5, end = '')
        for i in range(self.V + 2):
            print('{:4d}'.format(i), end='')
        
        print()

        for v, line in enumerate(self.matrix):
            print('{:4d}'.format(v), end=' ')
            for w, item in enumerate(line):
                print('{:4d}'.format(item), end='')
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