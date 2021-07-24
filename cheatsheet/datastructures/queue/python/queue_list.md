# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; List를 활용한 Queue 구현

> 해당 문서의 내용은 엄밀히 말해 Queue를 구현하는 것이 아니라, 파이썬의 내장 자료형인 List를 Queue의 특성에 맞게 사용하는 방법임.

## 1. 큐 생성 

```py
queue = []          # empty queue
queue = [1, 2, 3]   # queue initialize
```

* `queue[0]`가 큐의 front가 됨.

* `queue[2]`가 큐의 back이 됨.


<br/>

## 2. 큐 연산

> push: 리스트의 맨 앞부터 데이터를 추가
>
> pop: 리스트의 맨 앞 요소를 pop

```py
top = queue[-1]     # queue front
item = queue.pop()   # pop front item in queue
queue.append(4)     # queue push
len(queue) == 0     # isempty
```
