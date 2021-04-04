# Data Structrue

## 1. Array

### a. 1차원 배열

1. Python : List(Mutable Object)

    * 선언
        ```py
        a = []
        a = list()
        ```

    * 추가
        ```py
        a.append(1) # [1]
        a.append(2) # [1, 2]

        b = a * 3 # [1, 2, 1, 2, 1, 2]
        c = [3]
        a + c # [1, 2, 3]
        ```

    * 슬라이싱
        ```py
        a = [1, 2, 3, 4, 5]
        b = a[0:2] # [1, 2] 리스트 새로 생성하여 반환
        ```

    * mutable object, immutable object, interning 개념 : [링크](https://towardsdatascience.com/python-memory-and-objects-e7bec4a2845)
    
        * 파이썬에서 mutable object를 쓸 때는 이거 주의해야 함!
            ```py
            a = [1, 2, 3]
            b = a # b = [1, 2, 3]

            # id(a) == id(b)
            a.append(4)
            print(b) # [1, 2, 3, 4]

            b.append(5)
            print(a) # [1, 2, 3, 4, 5]
            ```

        * 변수 a, b가 동일한 mutable object를 가리키는 레퍼런스이기 때문

    * 복사 (Shallow Copy & Deep Copy)
        * Shallow Copy Examples
            ```py
            a = [1, 2, 3]
            b = a
            c = a.copy()

            a is b # True
            a is c # False
            a == c # True
            ```
            * `== 연산자` : 두 객체의 content나 value가 동일한지
            * `is 연산자` : 두 객체가 동일한 객체인지

### b. 2차원 배열 (Two Dimensional Array)
1. Python : List (Mutable Object)

    * 선언
        ```py
        # 0 ~ n-1 까지의 이차원 리스트 0으로 초기화
        a = [[0] * n for i in range(n)]
        b = [[0 for _ in range(n)] for __ in range(n)]

        # c = [[0] * n] * n # 이 표현은 2차원 배열을 생성하고자 할 때 사용 불가능!
        # [[0] * n]이 compound object 이고, list의 multiplication operator인 '*'이 shallow copy 동작을 수행하기 때문!
        ```
        
        <details>
        <summary>more</summary>

        ```py
        a = [[0] * n for _ in range(n)]
        b = [[0 for _ in range(n)] for __ in range(n)]
        c = [[0] * n] * n

        for i in range(n):
            print(hex(id(a[i])), hex(id(b[i])), hex(id(c[i])))

        """
        i   id(a[i])    id(b[i])    id(c[i])
        0   0x10ae76400 0x10ae76740 0x10ae83c80
        1   0x10ae838c0 0x10ae83cc0 0x10ae83c80
        2   0x10ae83480 0x10ae61b80 0x10ae83c80
        3   0x10ae83a00 0x10ae83b40 0x10ae83c80
        4   0x10ae83d80 0x10ae83840 0x10ae83c80
        """
        ```
        
        </details>

## 2. Stack


## 3. Queue


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