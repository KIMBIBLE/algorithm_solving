
# DFS(Depth-first Search) 알고리즘

Tree 및 Graph 등의 자료구조에 대한 <u><b>경로 탐색</b></u>에 활용되는 알고리즘. DFS는 특정 노드에서 시작하여, 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식으로 그래프를 탐색하는 특징을 가지고 있음. DFS는 현재 경로상의 노드만 기억하면 되기 때문에, BFS에 비해 저장 공간이 적게 필요하다는 장점을 가지고 있음. 하지만 단순 검색 속도는 BFS보다 느리며, 해를 구하면 탐색이 종료되는 방식으로 구현되기 때문에 구한 해가 최단 경로라는 보장이 되지 않음.(목표에 대한 경로가 여러 개일 경우, 반드시 최적해를 구한다고 보장하지 못함.)

<br/>

## ***1. Idea for DFS algorithm***

### 1. DFS 탐색을 위한 자료형

DFS 탐색을 위해 다음의 두 가지 탐색 상태를 저장하는 과정이 필요하다.

1. 이후 방문할 노드들을 기록하는 자료형

    DFS 알고리즘은 현재 노드에 해당되는 분기를 먼저 탐색하고, 인접한 노드를 탐색하는 방식으로 동작한다. 따라서 DFS 알고리즘은 스택 자료형을 활용하여, 현재 노드를 기준으로 이후 탐색할 노드들을 가장 나중에 방문하고 싶은 노드 순부터 저장하면, 스택에 넣은 역순으로 노드들을 방문할 수 있다.

    한편, 스택을 활용하여 DFS를 구현할 경우, 스택에는 항상 방문되지 않은 노드들이 위치한다고 보장하지 않는다. 따라서 이후 스택에서 노드를 pop한 시점에서 해당 노드가 방문되었는지 체크하는 로직이 필요하다.(이미 방문된 노드라면 pop된 상태 그대로 다음 반복을 수행하여, 백트래킹이 가능하게 함.)

<br/>

2. 노드들의 방문여부를 관리하는 자료형

    DFS 탐색 알고리즘은 인접한 노드들을 늦게 방문하고 싶은 순서대로 스택에 삽입한다. 이에 따라 특정 노드에 대해 인접한 노드가 2개 이상인 경우, 이후 방문할 노드들을 기록하는 스택 자료형에 중복으로 노드가 들어갈 수 있다. 따라서 노드들의 방문여부를 지속적으로 관리해주기 위한 추가적인 자료형이 필요하다.

    DFS 알고리즘은 노드들의 방문여부를 관리하는 자료형를 활용하여, 이후 방문할 노드들을 기록하는 스택에 인접한 노드들 중 방문되지 않은 노드들만을 삽입하여 동일한 노드에 중복으로 방문하는 경우를 방지할 수 있다.

<br/>

### 2. DFS 탐색의 동작 과정

- 루트 노드를 기준으로 탐색 시작 (그래프의 경우 임의의 노드를 지정)

- 현재 노드를 기준으로 갈 수 있는 만큼 노드 탐색을 수행하고, 더 이상 못가는 지점에 도달한다면 백트래킹을 수행(`pop/ret`).

- 아직 방문하지 않은 모든 노드들에 대해 해당 과정 반복


<br/>

:bulb:&ensp; 참고 1: DFS 탐색 알고리즘에서 `방문`과 `노드 출력`은 동일한 시점(스택에서 pop한 노드가 방문되지 않았을 때)에 처리할 수 있다.

<br/>

:bulb:&ensp; 참고 2: 특정 노드에서 이동 가능한 노드가 2가지 이상이 있을 때, DFS의 방문 기준은 해당 부분에서 스택(`방문할 노드 시퀀스`)에 어떤 순서로 삽입하느냐에 따라 달라짐.

</br>

---
## 2. Iterative DFS 구현

### 1. Iterative DFS 구현: Adjacency List

```py
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
```

<br/>

### 2. Iterative DFS 구현: Adjacency Matrix

```py
class Graph:
    VISITED = True
    UNVISITED = False
    LINKED = True
    UNLINKED = False

    def __init__(self, V):
        self.V = V # 정점의 갯수, 정점은 1부터 시작
        self.matrix = [ [ Graph.UNLINKED for _ in range(self.V + 1) ] for _ in range(self.V + 1)]
        self.visited = [Graph.UNVISITED for _ in range(self.V + 1)]

    def addEdge(self, v, w):
        self.matrix[v][w] = Graph.LINKED
        self.matrix[w][v] = Graph.LINKED # bi-directional graph

    # 정점 s로부터 아직 방문하지 않은 모든 노드에 대한 방문 수행
    def dfs(self, s = 1):
        stack = [s]

        while stack:
            #print('stack: {}'.format(stack))
            s = stack.pop() # 현재 노드

            # 현재 노드가 방문하지 않은 노드라면: 방문처리 + 노드출력 + 이후 방문할 노드 삽입
            if self.visited[s] == Graph.UNVISITED: 
                self.visited[s] = Graph.VISITED
                print('visit: node {}'.format(s))

                # 현재 노드와 연결되어 있는 노드 중, 아직 방문하지 않은 노드를 스택에 추가
                for node in range(self.V, 0, -1): # V, V-1, ...., 1
                    if self.matrix[s][node] == Graph.LINKED and self.visited[node] == Graph.UNVISITED:
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
```

<br/>

---
## 3. Recursive DFS 구현

탐색 시작 정점부터 시작하여 연결된 노드들이 아직 방문하지 않은 노드라면 DFS 탐색 수행.

<br/>

### 1. Recursive DFS 구현: Adjacency List

```py
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
```

<br/>

### 2. Recursive DFS 구현: Adjacency Matrix

```py
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
```

<br/>

---
## 4. DFS 알고리즘은 언제 사용할까?

- 그래프의 완전 탐색 시 활용 가능

- 그래프의 연결 요소 개수 구할 때 활용 가능

- 가중치(`weighted`) 그래프의 경우, 그래프의 DFS traversal은 최소 신장 트리(`mininum spanning tree`)와 최단 경로(`shortest path`) tree의 모든 쌍을 구할 수 있음.
  <details>
  <summary>Spanning Tree?</summary>

  - 신장 트리(Spanning Tree): 그래프의 최소 연결 부분 그래프(그래프에서 일부 간선을 선택하여 만든 그래프)
  
  - spanning tree의 조건?
    - 원본 그래프의 모든 노드를 포함
    - 모든 노드가 서로 연결되어있어야 함
    - 트리 속성을 만족(사이클이 없어야 함)
  
  -  최소 신장 트리(`Minimun Spanning Tree`)?: Spanning Tree 중에 간선의 가중치 합이 최소인 트리
      > 엣지의 가중치의 합이 최소인 신장 트리

  - 원본 그래프에서 MST(Minimum Spanning Tree)를 찾아내는 대표적 기법에는 `크루스칼 알고리즘(Kruskal's algorithm)`과 `Prim's algorithm`이 있음.
  </details>

- 그래프의 cycle 검사
  - 그래프에는 DFS 수행 중 백엣지(`back edge`)가 표시되는 경우에만 사이클이 있음. 따라서, 그래프에 대해 DFS를 수행하고, 백엣지(`back edge`)를 검사하는 방법을 사용하면 됨.
  - [참고 링크](http://people.csail.mit.edu/thies/6.046-web/recitation9.txt)

- 경로 탐색(Path Finding)
  - vertex u, z가 주어졌을 때, 두 vertex간의 경로를 탐색하기 위해 DFS를 사용 가능

- 위상 정렬(Topology Sort)

- 이분 그래프(Bipartite Graph) 테스트

- 그래프의 강한 결합/연결 요소(Strongly Connected Component) 찾기

- 해답이 1개인 퍼즐 풀기
  - 미로 관련 문제, 장애물이 있는 matrix
