# deque를 활용한 Stack 구현

## 1. 스택 생성 

```py
from collections import deque
stack = deque([1, 2, 3])
```

## 2. 스택 연산

```py
top = stack[-1]     # stack pop
top = stack.pop()   # stack top
stack.append(4)     # stack push
len(stack)          # isempty
```