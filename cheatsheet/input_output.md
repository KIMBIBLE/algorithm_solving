# Input

## 1. Integer

### a. Python
* 정수 입력
```py
type(input()) # <class 'str'>
n1 = int(input())
n2, n3 = map(int, input().split())

import sys
type(sys.stdin.readline()) # <class 'str'>
readline = lambda: sys.stdin.readline()
n4 = int(readline())
n5, n6 = map(int, readline().split())
```

## 2. Array
* 정수 입력
```py
import sys
lambda readline: sys.stdin.readline()

n, m = map(int, readline().split())
arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = int(readline())
```


### a. Python

# Output
