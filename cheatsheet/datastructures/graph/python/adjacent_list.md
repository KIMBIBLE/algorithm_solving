# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; Graph의 인접 리스트(Adjacent List) 구현

그래프는 파이썬에서 내장 자료형으로 제공하지 않기 떄문에 직접 구현해줘야 함.

<br/>


## :one:&ensp; 입력 포맷

* 코딩테스트 Graph 문제의 입력값 제공 방식에 대한 기본 예시: [more samples](../../../input_output_style/input_output.md)

    ```txt
    4 5 1
    1 2
    1 3
    1 4
    2 4
    3 4
    ```

    * `line 1`

      *  `N`: Node 갯수

      *  `M`: 간선의 갯수

      *  `V`: 탐색을 시작할 정점

    * `line 2 ~ line M+1`: 간선을 연결하는 `두 정점의 번호`

<br/>


## :two:&ensp; 인접 리스트(adjacent List)

```py
import sys
readline = lambda: sys.stdin.readline()
N, M, V = map(int, readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    src, dest = map(int, readline().split())
    graph[src].append(dest)
    graph[dest].append(src)
```
* `graph = [[] for _ in range(N + 1)]`

    코테 문제에서는 정점의 번호가 `1부터 시작`하는 경우가 많음. 따라서 인접 행렬 방식으로 그래프를 생성할 때, 행렬을 하나씩 추가해줘서 정점에 번호와 일치하도록 행렬의 index를 사용하는 것이 편리함.