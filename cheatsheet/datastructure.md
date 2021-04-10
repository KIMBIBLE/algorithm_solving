# Data Structrue

## 1. Array

### a. 1차원 배열

1. Python : List(Mutable Object)

    * 선언
        ```py
        a = []
        a = list()
        a = [] * 10 # []
        a = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a = [[]] * 10 # [[], [], [], [], [], [], [], [], [], []]
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
1. Python
    * List
        ```py
        stack = [] # empty stack
        stack = [1, 2, 3]   # stack initialize

        top = stack.pop()   # stack pop
        top = stack[-1]     # stack top
        stack.append(4)     # stack push
        len(stack) == 0     # isempty
        
        # 
        ```
        * isfull은 일반적인 경우 코테에서는 고려하지 않아도 됨!
        * 32비트 시스템에서 python의 list는 536,870,912까지 저장 가능!
        * 64비트 시스템의 경우 : 9,223,372,036,854,775,807
            ```py
            >>> import platform
            >>> platform.architecture()
            ('64bit', '')
            >>> sys.maxsize
            9223372036854775807
            ```
        * [python src](https://svn.python.org/projects/python/trunk/Objects/listobject.c?revision=69227&view=markup)
          <details>
            <summary>more</summary>

            ```cpp
            /* Ensure enough temp memory for 'need' array slots is available.
            * Returns 0 on success and -1 if the memory can't be gotten.
            */
            static int
            merge_getmem(MergeState *ms, Py_ssize_t need)
            {
                assert(ms != NULL);
                if (need <= ms->alloced)
                    return 0;
                /* Don't realloc!  That can cost cycles to copy the old data, but
                * we don't care what's in the block.
                */
                merge_freemem(ms);

                /* 
                 * 여기 코드에 최대 할당 가능한 사이즈가 나옴!
                 * (size_t)need > PY_SSIZE_T_MAX / sizeof(PyObject*)
                 * 
                 * in <pyport.h>
                 * Largest positive value of type Py_ssize_t.
                 * #define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))
                 * 
                 */
                 
                if ((size_t)need > PY_SSIZE_T_MAX / sizeof(PyObject*)) {
                    PyErr_NoMemory();
                    return -1;
                }
                ms->a = (PyObject **)PyMem_Malloc(need * sizeof(PyObject*));
                if (ms->a) {
                    ms->alloced = need;
                    return 0;
                }
                PyErr_NoMemory();
                merge_freemem(ms);          /* reset to sane state */
                return -1;
            }
            ```
          </details>
    * deque
        ```py
        from collections import deque
        ```

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