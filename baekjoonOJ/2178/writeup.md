# BOJ-2178: 미로 탐색

## :one:&ensp; 제약조건 분석

### 1. 제약조건

* 시간 제한: 1 sec
* 메모리 제한: 198 MB

<br/>

### 2. 제약조건에서 활용 가능한 알고리즘

제약조건 분석 내용 작성

<br/>

---
## :two:&ensp; 입출력

### 1. 입력

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

<br/>

### 2. 출력

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.


<br/>

---
## :three:&ensp; 문제 분석

### 1. 문제

N×M크기의 배열로 표현되는 미로가 있다.

|||||||
|-|-|-|-|-|-|
|1|0|1|1|1|1|
|1|0|1|0|1|0|
|1|0|1|0|1|1|
|1|1|1|0|1|1|

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

<br/>

### 2. 입출력 예제

:bulb:&ensp; ***Case 1: xxx한 입력의 경우***

* 입력 
    
    ```
    4 6
    101111
    101010
    101011
    111011
    ```

* 출력: `15`

<br/>

:bulb:&ensp; ***Case 2: xxx한 입력의 경우***

* 입력
    
    ```
    4 6
    110110
    110110
    111111
    111101
    ```

* 출력: `9`

    ```
    <output>
    ```

<br/>

### 3. 문제 분석

전형적인 bfs를 통한 최단경로 찾기 문제. bfs의 level이 증가할 때마다 1씩 누적하면 됨. 미로 표현 시, oob access를 방지하기 위해 구현로직에 예외 처리를 해주거나, 앞뒤로 2칸씩 이동 불가능한 위치를 넣어주는 방식으로 구현 가능.

<br/>

### 4. 구현전 blueprint


```py
# 문제에 주어진 바에 따라 미로 표현

UN_AVAILABLE    = 0
AVAILABLE       = 1
START_POS       = -1 # 나중에 미로 찾기 시작할 때, 시작 지점에서 이동하는 경우, 다음 위치 값을 2로 수동으로 처리해줘야함.
```

```py
# x, y 움직임에 대한 offset 표현
move = [(1, 0), (-1, 0) (0, -1), (0, 1)] # 상하좌우 이동
```

<br/>

---
## :four:&ensp; 문제 구현 코드

```py
import sys
readline = lambda: sys.stdin.readline().rstrip()
from collections import deque

class Graph:
    UNAVAILABLE    = 0
    AVAILABLE       = 1
    START_LEVEL     = -1

    def __init__(self):
        self.n, self.m = map(int, readline().split()) # n행, m열

        # n+2 행, m+2 열 배열 생성: access 불가능한 경계선 추가
        self.matrix = [[Graph.UNAVAILABLE for _ in range(self.m + 2)]]
        for _ in range(self.n):
            data = list(map(int, list(readline())))
            self.matrix.append([Graph.UNAVAILABLE] + data[:] + [Graph.UNAVAILABLE])

        self.matrix.append([Graph.UNAVAILABLE for _ in range(self.m + 2)])

    
    def bfs(self):
        move = [(0, 1), (0, -1), (-1, 0), (1, 0)] # dx, dy: 상하좌우 이동
        queue = deque()
        queue.append((1, 1)) # start pos(x, y)
        self.matrix[1][1] = Graph.START_LEVEL

        while queue:
            cur_x, cur_y = queue.popleft()
            if cur_x == self.m and cur_y == self.n:
                return self.matrix[cur_y][cur_x] # 도착
            
            for offset in move:
                next_x = cur_x + offset[0]
                next_y = cur_y + offset[1]
                if self.matrix[next_y][next_x] == Graph.AVAILABLE:
                    queue.append((next_x, next_y))

                    if self.matrix[cur_y][cur_x] == Graph.START_LEVEL:
                        self.matrix[next_y][next_x] = 2
                    else:
                        self.matrix[next_y][next_x] = self.matrix[cur_y][cur_x] + 1

    
    def show(self):
        for line in self.matrix:
            for item in line:
                print('{:4d}'.format(item), end='')
            print()



if __name__ == '__main__':
    graph = Graph()
    graph.show()
    print(graph.bfs())
    graph.show()
```

<br/>

---
## :five:&ensp; 문제 사후 분석

### 1. 다른사람 코드 분석

:bulb:&ensp; ***AAA 접근 방식***

```py

```

:bulb:&ensp; ***BBB 접근 방식***

```cpp

```

<br/>

### 2. 해당 문제 해결을 위해 알아야하는 개념의 카테고리 정리

ex) 배열 인덱스 계산, swap, 다이나믹 프로그래밍-Unique Paths Problem...

<br/>

---
## 참고

* [원본문제 링크](https://www.acmicpc.net/problem/2178)