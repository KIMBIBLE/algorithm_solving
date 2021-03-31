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


# Output
