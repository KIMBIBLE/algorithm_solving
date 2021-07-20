# Input

## 1. Integer

### a. Python

* 정수 입력

```py
type(input()) # <class 'str'>
n1 = int(input())
n2, n3 = map(int, input().split())
n4, n5, n6, n7, n8 = map(int, [input() for _ in range(5)])
l = list(map(int, input().split()))

import sys
type(sys.stdin.readline()) # <class 'str'>
readline = lambda: sys.stdin.readline().rstrip()
readline = lambda: sys.stdin.readline()
n4 = int(readline())
n5, n6 = map(int, readline().split())
```

## 2. Array

### a. Python

* 이차원 배열에 정수 입력 받기

  * Case 1: 각 라인에 구분자가 없는 경우

    ```
    4 6
    101111
    101010
    101011
    111011
    ```

    ```py
    import sys
    readline = lambda: sys.stdin.readline()
    n, m = map(int, readline().split())
    a = [list(map(int, input())) for _ in range(n)]
    # list(map(int, "12345")) 를 생각해보면 쉬움!
    ```

  * Case 2: 가장 일반적인 케이스로 구분자가 `' '`인 경우
    
    ```
    4 3
    0 1 0
    1 2 3
    4 3 2
    ```

    ```py
    import sys
    lambda readline: sys.stdin.readline().rstrip()

    n, m = map(int, readline().split())
    arr = [[0] * m for _ in range(n)]

    # Multiline 
    for i in range(n):
        for j in range(m):
            arr[i][j] = int(readline())

    # Oneline
    n, m = map(int, readline().split())
    a = [list(map(int, readline().split())) for _ in range(n)]

    ```

  * Case 3: 몇개 입력할지 알려주지 않고, 입력이 끝날 때 까지 입력을 받는 경우(`EOF`)
    
    ```py
    import sys
    readline = lambda: sys.stdin.readline()
    x = []

    while True:
        line = readline()
        if line:
            x.append(line.split())

        # When eof is encountered, the result of readline() is an empty string("").
        else:
            break
    ```

## 2. Graph

### a. Python

* type 1: programmers

  * case a

    ```
    n: 3 
    data: [[1,1,0], [1,1,0], [0,1,2]
    ```

* type 2: boj

  * case a

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

# Output

## 1. 요소마다 개행('\n')을 붙여서 출력

### a. Python
  
* print() 일반 출력 예시
  
  ```py
  for i in range(3):
      print i
  
  # result
  # 0
  # 1
  # 2
  ```

## 1. 모든 요소를 한줄에 출력

### a. Python
  
* `Python2`: print에 comma를 붙여 사용

  ```py
  for i in range(5):
    print i,
  
  # result
  # 0 1 2 3 4
  ```

* `Python3`: print의 `end` 인자 활용

  ```py
  for i in range(5):
    print(i, end = ' ')

  # result
  # 0 1 2 3 4
  ```