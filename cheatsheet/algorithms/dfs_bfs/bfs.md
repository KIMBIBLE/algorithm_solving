
# BFS(Breadth First Search) 알고리즘

> Tree 및 Graph 등의 자료구조에 대한 <u><b>경로 탐색</b></u>에 활용되는 알고리즘

## &nbsp; ***1. Overview***
- 인접한 노드를 우선적으로 방문
- 일반적인 경우 dfs보다 bfs가 속도 면에서 유리

## ***2. Idea for BFS algorithm***
- 탐색 시작 노드를 큐에 삽입하고, 방문 처리

- 큐에 노드가 남아 있을 때까지 과정 반복
  - 큐에서 pop한 노드를 `출력`
  - 큐에서 pop한 노드에 대해 인접한 노드들을 모두 `큐에 삽입`과 함께 `방문처리`
  
  <details>
    <summary>Python Implementation ❤️ </summary>

    ```py
    from collections import deque

    class Graph:
      def __init__(self, V):
        self.V = V
        self.adj = [ [] for _ in range(V + 1)]
        self.visited = [False] * (V + 1)

        def addEdge(self, v, w):
          self.adj[v].append(w)
          self.adj[w].append(v)

        def bfs(self, s = 1):
          queue = deque([s])
          self.visited[s] = True

          while queue:
            cur_node = queue.popleft()
            print(cur_node, end = ' ')

            for linked_node in self.adj[cur_node]:
              if self.visited[linked_node] == False:
                queue.append(linked_node)
                self.visited[linked_node] = True


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

    g.bfs() # 1 2 3 8 7 4 5 6
    ```

  </details>

  </br>

## ***3. BFS 알고리즘은 언제 사용할까?***

- 그래프의 완전 탐색 시 활용 가능

- 그래프의 연결 요소 개수 구할 때 활용 가능

- 그래프의 `최단거리 탐색 시` 활용 가능
  - 가장 짧은 뎁스의 노드를 발견하자마다 탐색을 중단하면 됨.
