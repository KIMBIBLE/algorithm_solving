# 1차원 배열의 탐색: 순차탐색

> 배열 내 데이터를 찾기 위해 배열의 맨 앞에서부터 차례로 데이터를 검색하는 탐색방식. <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />의 시간복잡도를 가짐.

## :one:&ensp; 탐색 코드

### 1. 직접 구현

```py
array = ['asdf', 'qwer', 'wert', 'bbkim', 'erty']
target = 'bbkim'

def sequential_search(array, target):
    for idx, each in enumerate(array):
        if each == target:
            return idx

    return -1


pos = sequential_search(array, target)
print('target {}\'s index: {}'.format(target, pos))
# target bbkim's index: 3

target = 'bhui'
pos = sequential_search(array, target)
print('target {}\'s index: {}'.format(target, pos))
# target bhui's index: -1

```

<br/>

### 2. 리스트의 index() 메서드를 활용

> 리스트 내의 데이터를 index() 메서드를 활용하여 탐색할 수 있음. 하지만 index() 메서드를 활용하면 탐색에 실패한 경우, `ValueError` Exception이 발생하기 때문에, 탐색에 실패한 케이스에 대해 Exception Handling을 직접 해줘야 함.

```py
array = ['asdf', 'qwer', 'wert', 'bbkim', 'erty']
target = 'bbkim'

pos = sequential_search(array, target)
print('target {}\'s index: {}'.format(target, array.index(target)))
# target bbkim's index: 3


target = 'bhui'
print('target {}\'s index: {}'.format(target, array.index(target)))
"""
Traceback (most recent call last):
  File "sequential_search.py", line 20, in <module>
    print('target {}\'s index: {}'.format(target, array.index(target)))
ValueError: 'bhui' is not in list
"""
```