# Data Structrue

## :one:&ensp; 배열

### 1. Python

* [1차원 배열의 주요 메서드와 특징: List](./datastructures/python/array/one_dimensional_array.md)

* [다차원(2차원 이상) 배열의 생성 및 사용: List](./datastructures/python/array/multi_dimensional_array.md)

* [(외부 링크) Python, Memory, and Objects](https://towardsdatascience.com/python-memory-and-objects-e7bec4a2845): mutable object, immutable object, interning 개념 설명 잘되어있음.

* [(외부 링크) assignment("=") vs shallow copy vs deep copy](https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86)


<br/>

---
## :two:&ensp; 스택

### 1. Python

* [List를 활용한 구현](./datastructures/python/stack/stack_list.md)

* [deque 모듈 사용](./datastructures/python/stack/stack_deque.md)

<br/>

---
## :two:&ensp; 큐

* [List를 활용한 구현](./datastructures/python/queue/queue_list.md)

* [deque 모듈 사용](./datastructures/python/queue/queue_deque.md)
* 
<br/>

---
## :three:&ensp; 그래프



<br/>

---
## :four:&ensp; 트리


---

<br/>

## :five:&ensp; 해시 테이블


---

<br/>


## 3. Queue
1. Python
    * List
    * 



## 4. Graph

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

### b. 인접 행렬(adjacent Matrix)
1. Python
    ```py
    import sys
    readline = lambda: sys.stdin.readline()
    N, M, V = map(int, readline().split())
    graph = [[0] * (M + 1) for _ in range(M + 1)]

    for _ in range(0, M):
        src, dest = map(int, readline().split())
        graph[src][dest] = 1
        graph[src][dest] = 1

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

### d. 간선 리스트(Edge List)
1. Python
    ```py
    ```

### e. Edge Cases

## 5. Tree
1. Python
   ```py

   ```