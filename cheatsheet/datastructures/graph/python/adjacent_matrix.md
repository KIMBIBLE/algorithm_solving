
### a. 입력 포맷
* 기본 예시([more samples](./input_output.md))
```
line 1 -> N: Node 갯수, M: 간선의 갯수, V: 탐색을 시작할 정점
line 2 ~ line M+1 -> 간선을 연결하는 두 정점의 번호
4 5 1
1 2
1 3
1 4
2 4
3 4
```



### c. 인접 리스트(adjacent List)
1. Python
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
