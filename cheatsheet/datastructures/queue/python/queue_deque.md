# deque를 활용한 Queue 구현

## 1. 큐 생성 

```py
from collections import deque
queue = deque([1, 2, 3])
```

## 2. 큐 연산

```py
top = queue.popleft()   # front item in queue
top = queue[-1]         # pop front item in queue
queue.append(4)         # queue push
len(queue)              # isempty
```