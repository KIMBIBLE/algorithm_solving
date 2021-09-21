class Graph:
    def __init__(self, V):
        self.V = V # 정점의 갯수, 정점은 1부터 시작
        self.adj = [ [] for _ in range(self.V + 1)]
        self.visited = [False for _ in range(self.V + 1)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v) # bi-directional graph

    # 정점 s로부터 아직 방문하지 않은 모든 노드에 대한 방문 수행
    def dfs(self, s = 1):
        stack = [s]

        while stack:
            print('stack: {}'.format(stack))
            s = stack.pop() # 현재 노드

            # 현재 노드가 방문하지 않은 노드라면: 방문처리 + 노드출력 + 이후 방문할 노드 삽입
            if self.visited[s] == False: 
                self.visited[s] = True
                print('visit: node {}'.format(s))

                # 현재 노드와 연결되어 있는 노드 중, 아직 방문하지 않은 노드를 스택에 추가
                for node in self.adj[s][::-1]:
                    if self.visited[node] == False:
                        stack.append(node)


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
