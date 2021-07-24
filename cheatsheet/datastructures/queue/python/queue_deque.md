# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; `collections.deque`를 활용한 Queue 구현 및 Operation Time Complexity

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

## 3. Time Complexity

A deque (double-ended queue) is represented `internally as a doubly linked list`. (Well, `a list of arrays rather than objects, for greater efficiency`.) Both ends are accessible, but even looking at the middle is slow, and adding to or removing from the middle is slower still.

|Operation  |Average Case   |Amortized Worst Case   |
|:-:        |:-:            |:-:                    |
|Copy       |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|append     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|appendleft |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|pop        |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|popleft    |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|extend     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(k)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k)" />|
|extendleft |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(k)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k)" />|
|rotate     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(k)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k)" />|
|remove     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|

<br/>

---
## 참고

* https://wiki.python.org/moin/TimeComplexity