
# DFS(Depth-first Search) 알고리즘

> Tree 및 Graph 등의 자료구조에 대한 <u><b>경로 탐색</b></u>에 활용되는 알고리즘

## ***1. Overview***
- 루트 노드를 기준으로 탐색 시작 (그래프의 경우 임의의 노드를 지정)
- 현재 노드를 기준으로 갈 수 있는 만큼 노드 탐색을 수행하고, 더 이상 못가는 지점에 도달한다면 백트래킹을 수행(`pop/ret`).
- 아직 방문하지 않은 모든 노드들에 대해 해당 과정 반복

</br>

## ***2. Iterative DFS 구현***
<details>
  <summary>Show Example Graph</summary>

  <p align="center">
    <img width="50%" src="../figure/graph_example_01.png"/>
  </p>
</details>

<details>
  <summary>💡&ensp; Implementation Idea</summary>

  > - 방문은 언제 수행?: 스택에서 pop한 노드가 방문되지 않았을 때
  > 
  > - 노드 출력은 언제?: 스택에서 pop한 노드가 방문되지 않았을 때
  > 
  > - 앞으로 방문해야 할 노드가 남은 경우에 대한 반복 처리 로직은 크게 2가지 부분으로 구성됨.
  > 
  >   - 먼저, stack에서 pop한 방문해야 할 노드가 방문하지 않은 노드인 경우?
  >     - 방문/출력 처리
  > 
  >     - 해당 노드와 연결된 노드 중 방문하지 않은 노드를 앞으로 방문해야 할 노드를 저장하는 스택에 push
  > 
  >   - 다음으로, stack에서 pop한 방문해야 할 노드가 방문한적이 있는 노드인 경우?
  > 
  >     - 다음 반복을 수행: stack에 저장된 방문해야 할 노드 하나를 pop하였기 때문에, backtracing을 하는 동작으로 이해하면 편함.


  - `stack` 생성 및 초기화
    - `stack`: 방문을 진행하고자하는 노드들을 저장할 스택 생성(뒤에서부터 방문).
    - 첫 번째로 방문을 수행할 노드를 스택에 삽입

  - 스택에 저장한 방문할 노드가 남아있는 동안 반복 수행
    - 스택의 최상단 노드를 `pop`하고, 해당 노드가 아직 방문하지 않은 노드라면 `방문처리`.
      - *"DFS의 노드 탐색 순서를 출력해야 하는 경우, pop된 요소를 `출력`하면 됨."*
    - 스택에서 `pop`된 노드(`current node`)를 기준으로, 인접해있는 모든 노드 중 아직 방문하지 않은 노드를 모두 스택에 `push`.
      - *"특정 노드에서 이동 가능한 노드가 2가지 이상이 있을 때, DFS의 방문 기준은 해당 부분에서 스택(`방문할 노드 시퀀스`)에 어떤 순서로 삽입하느냐에 따라 달라짐."*
</details>


- Implementation 1

  <details>
    <summary>Python Code</summary>

    ```py
    class Graph:
      def __init__(self, V, is_bidirect = True):
        self.V = V # 정점의 갯수, 정점은 1부터 시작
        self.adj = [ [] for _ in range(self.V + 1)]
        self.is_bidirect = is_bidirect
        self.visited = [False for _ in range(self.V + 1)]


      def addEdge(self, v, w):
        self.adj[v].append(w)
        if self.is_bidirect == True:
          self.adj[w].append(v) # bi-directional graph

      # 정점 s로부터 아직 방문하지 않은 모든 노드에 대한 방문 수행
      def dfs(self, s = 1):
        stack = [s] # 방문할 예정인 노드들
        
        while stack:
          s = stack.pop()

          """
          스택에서 pop된 노드가 아직 방문하지 않은 노드인 경우만 출력.
          스택에 동일한 정점이 2번 들어갈 수 있기 때문.
          """
          if (not self.visited[s]):
            print(s, end=" ")
            self.visited[s] = True

          """
          정점 s와 연결된 모든 정점에 대해 순차적으로
          해당 정점이 아직 방문하지 않은 정점이라면, 스택에 삽입함.
          """
          for node in self.adj[s][::-1]:
            if (not self.visited[node]):
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

  </details>

  <details>
    <summary>Result</summary>

    ```
    stack: [1]
    pop: node 1 -> visit
    visited_seq: [1]
    push: node 8
    push: node 3
    push: node 2

    stack: [8, 3, 2]
    pop: node 2 -> visit
    visited_seq: [1, 2]
    push: node 7

    stack: [8, 3, 7]
    pop: node 7 -> visit
    visited_seq: [1, 2, 7]
    push: node 8
    push: node 6

    stack: [8, 3, 8, 6]
    pop: node 6 -> visit
    visited_seq: [1, 2, 7, 6]

    stack: [8, 3, 8]
    pop: node 8 -> visit
    visited_seq: [1, 2, 7, 6, 8]

    stack: [8, 3]
    pop: node 3 -> visit
    visited_seq: [1, 2, 7, 6, 8, 3]
    push: node 5
    push: node 4

    stack: [8, 5, 4]
    pop: node 4 -> visit
    visited_seq: [1, 2, 7, 6, 8, 3, 4]
    push: node 5

    stack: [8, 5, 5]
    pop: node 5 -> visit
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8, 5]
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8]
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]
    ```
  </details>

- Implementation 2 :heart:

  <details>
    <summary>Python Code</summary>

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
        #visited_seq = []

        while stack:
          #print('stack: {}'.format(stack))
          s = stack.pop()
          #print('current node: {}'.format(s))

          if self.visited[s] == False:
            self.visited[s] = True
            #visited_seq.append(s)
            #print('visit: node {}'.format(s))

            for node in self.adj[s][::-1]:
              if self.visited[node] == False:
                stack.append(node)
                #print('push: node {}'.format(s))

          #print('visited_seq: {}'.format(visited_seq))
          #print('')

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
  </details>

  <details>
    <summary>Result</summary>

    ```
    stack: [1]
    current node: 1
    visited: node 1
    push: node 1
    push: node 1
    push: node 1
    visited_seq: [1]

    stack: [8, 3, 2]
    current node: 2
    visited: node 2
    push: node 2
    visited_seq: [1, 2]

    stack: [8, 3, 7]
    current node: 7
    visited: node 7
    push: node 7
    push: node 7
    visited_seq: [1, 2, 7]

    stack: [8, 3, 8, 6]
    current node: 6
    visited: node 6
    visited_seq: [1, 2, 7, 6]

    stack: [8, 3, 8]
    current node: 8
    visited: node 8
    visited_seq: [1, 2, 7, 6, 8]

    stack: [8, 3]
    current node: 3
    visited: node 3
    push: node 3
    push: node 3
    visited_seq: [1, 2, 7, 6, 8, 3]

    stack: [8, 5, 4]
    current node: 4
    visited: node 4
    push: node 4
    visited_seq: [1, 2, 7, 6, 8, 3, 4]

    stack: [8, 5, 5]
    current node: 5
    visited: node 5
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8, 5]
    current node: 5
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8]
    current node: 8
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]
    ```
  </details>


- Implementation 3

  <details>
    <summary>Python Code</summary>

    ```py
    class Graph:
      def __init__(self, V, is_bidirect = True):
        self.V = V # 정점의 갯수, 정점은 1부터 시작
        self.adj = [ [] for _ in range(self.V + 1)]
        self.is_bidirect = is_bidirect
        self.visited = [False for _ in range(self.V + 1)]


      def addEdge(self, v, w):
        self.adj[v].append(w)
        if self.is_bidirect == True:
          self.adj[w].append(v) # bi-directional graph

      # 정점 s로부터 아직 방문하지 않은 모든 노드에 대한 방문 수행
      def dfs(self, s = 1):
        stack = [s]
        visited_seq = []

        while stack:
          print('stack: {}'.format(stack))
          s = stack.pop()
          print('current node: {}'.format(s))


          if self.visited[s] == False:
            self.visited[s] = True
            visited_seq.append(s)
            print('visit: node {}'.format(s))

            stack.extend(self.adj[s][::-1])
            print('push: node {}'.format(self.adj[s]))


          print('visited_seq: {}'.format(visited_seq))
          print('')

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

  </details>

  <details>
    <summary>Result</summary>

    ```
    stack: [1]
    current node: 1
    visit: node 1
    push: node [2, 3, 8]
    visited_seq: [1]

    stack: [8, 3, 2]
    current node: 2
    visit: node 2
    push: node [1, 7]
    visited_seq: [1, 2]

    stack: [8, 3, 7, 1]
    current node: 1
    visited_seq: [1, 2]

    stack: [8, 3, 7]
    current node: 7
    visit: node 7
    push: node [2, 6, 8]
    visited_seq: [1, 2, 7]

    stack: [8, 3, 8, 6, 2]
    current node: 2
    visited_seq: [1, 2, 7]

    stack: [8, 3, 8, 6]
    current node: 6
    visit: node 6
    push: node [7]
    visited_seq: [1, 2, 7, 6]

    stack: [8, 3, 8, 7]
    current node: 7
    visited_seq: [1, 2, 7, 6]

    stack: [8, 3, 8]
    current node: 8
    visit: node 8
    push: node [1, 7]
    visited_seq: [1, 2, 7, 6, 8]

    stack: [8, 3, 7, 1]
    current node: 1
    visited_seq: [1, 2, 7, 6, 8]

    stack: [8, 3, 7]
    current node: 7
    visited_seq: [1, 2, 7, 6, 8]

    stack: [8, 3]
    current node: 3
    visit: node 3
    push: node [1, 4, 5]
    visited_seq: [1, 2, 7, 6, 8, 3]

    stack: [8, 5, 4, 1]
    current node: 1
    visited_seq: [1, 2, 7, 6, 8, 3]

    stack: [8, 5, 4]
    current node: 4
    visit: node 4
    push: node [3, 5]
    visited_seq: [1, 2, 7, 6, 8, 3, 4]

    stack: [8, 5, 5, 3]
    current node: 3
    visited_seq: [1, 2, 7, 6, 8, 3, 4]

    stack: [8, 5, 5]
    current node: 5
    visit: node 5
    push: node [3, 4]
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8, 5, 4, 3]
    current node: 3
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8, 5, 4]
    current node: 4
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8, 5]
    current node: 5
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]

    stack: [8]
    current node: 8
    visited_seq: [1, 2, 7, 6, 8, 3, 4, 5]
    ```

  </details>

</br>

## ***3. Recursive DFS 구현***

<details>
  <summary>Show Example Graph</summary>

  <p align="center">
    <img width="50%" src="./figure/graph_example_01.png"/>
  </p>
</details>

<details>
  <summary>💡&ensp; Implementation Idea</summary>

  > - 탐색 시작 정점부터 시작하여 연결된 노드들이 아직 방문하지 않은 노드라면 DFS 탐색 수행

</details>

- Implementation 1 :heart:
  <details>
    <summary>Python Code</summary>

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

  </details>

<br/>

## ***4. DFS 알고리즘은 언제 사용할까?***
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
