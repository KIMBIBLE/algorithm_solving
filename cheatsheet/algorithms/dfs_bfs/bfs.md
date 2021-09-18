# BFS(Breadth First Search) 알고리즘

Tree 및 Graph 등의 자료구조에 대한 <u><b>경로 탐색</b></u> 등에 활용되는 알고리즘. BFS 알고리즘은 탐색 시작 노드에서 시작해서 `인접한 노드를 먼저 탐색`하는 방식으로 그래프 탐색을 수행한다. 다시 말해, BFS 알고리즘을 활용한 탐색은 시작 노드부터 탐색을 시작하여 거리에 따라 단계별로 탐색을 수행한다고 할 수 있다.

<br/>

:bulb:&ensp; 참고: 일반적인 경우 dfs보다 bfs가 속도 면에서 유리하다.

<br/>

---
## :one:&ensp; Idea for BFS algorithm

### 1. BFS를 위한 자료형

BFS 탐색을 위해 다음의 두 가지 탐색 상태를 저장하는 과정이 필요하다.

1. 이후 방문할 노드들을 기록하는 자료형

    BFS 알고리즘은 현재 노드를 기준으로 인접한 노드를 먼저 방문하는 방식으로 탐색을 수행한다. 따라서 `Queue 자료형`을 활용하여 현재 노드를 기준으로 다음 방문할 노드들을 기록하면, 큐에 넣은 순서대로 노드를 순차적으로 방문할 수 있다.(인접한 노드가 먼저 큐에 들어가기 때문에, 큐의 선입선출 특성 상 인접한 노드를 먼저 방문할 수 있음.)

    한편, 큐를 활용하여 BFS를 구현하는 경우, `큐에는 항상 방문되지 않은 노드만 들어갈 수 있도록` 만들어줘야 동일한 노드에 중복으로 방문하는 경우를 방지할 수 있다.

<br/>

2. 노드들의 방문여부를 관리하는 자료형

    BFS 탐색 알고리즘은 인접한 노드를 큐에 순차적으로 삽입하는 방식으로 동작하기 때문에, 특정 노드에 대해 인접한 노드가 2개 이상일 경우, 이후 방문할 노드들을 기록하는 큐 자료형에 중복으로 노드가 들어갈 수 있다. 따라서 노드들의 방문여부를 지속적으로 관리해주기 위한 추가적인 자료형이 필요하다.

    BFS 알고리즘은 노드들의 방문여부를 관리하는 자료형를 활용하여, 이후 방문할 노드들을 기록하는 큐에 인접한 노드들 중 `방문되지 않은 노드들`만을 삽입하여 동일한 노드에 중복으로 방문하는 경우를 방지할 수 있다.

<br/>

### 2. BFS 탐색의 동작 과정

- 탐색 시작 노드를 큐에 삽입하고, 방문 처리.

- `큐에 노드가 남아 있을 때까지` 다음 과정 반복.
  
  - 큐에서 pop한 노드를 `출력`(BFS 방식으로 노드를 탐색하는 문제의 경우, `큐에서 pop한 시점에서 노드를 활용`하면 됨).
  
  - 큐에서 pop한 노드에 대해 인접한 노드들을 모두 `큐에 삽입`과 함께 `방문처리`.
  
<br/>

:bulb:&ensp; 참고: BFS 탐색 알고리즘은 노드 방문처리하는 시점에서, 노드가 실제로 방문되는 것은 아님! `큐에서 pop한 시점에서 노드가 방문되는 것!`

<br/>

---
## :two:&ensp; BFS 구현

### 1. 인접 리스트 구현

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
        print(cur_node, end = ' ') # 노드 출력

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

</br>

----
## :three:&ensp; BFS 알고리즘은 언제 사용할까?

- 그래프의 완전 탐색 시 활용 가능

- 그래프의 연결 요소 개수 구할 때 활용 가능

- 그래프의 `최단거리 탐색 시` 활용 가능
  - 가장 짧은 뎁스의 노드를 발견하자마다 탐색을 중단하면 됨.
