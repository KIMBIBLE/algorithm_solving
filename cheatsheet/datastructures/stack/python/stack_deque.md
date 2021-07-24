# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; `collections.deque`를 활용한 Stack 구현

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