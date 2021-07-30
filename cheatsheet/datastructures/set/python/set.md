# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; Python `set` 자료형

Python은 집합에 관한 연산을 처리하는 기능을 내장 자료형인 `set`을 통해 제공한다. `set` 자료형의 구현은 `dict` 자료형의 구현 방식과 내부적으로 매우 유사함.

<br/>

## :one:&ensp; set 생성

```py
s1 = set([1, 2, 3]) # set initialize
print(s1)           # {1, 2, 3}

s2 = set("Hello")
print(s2)           # {'H', 'l', 'e', 'o'}
```

<br/>

---
## :two:&ensp; 집합 자료형 관련 함수들

### 1. 값 1개 추가하기(`add`)

```py
s1 = set([1, 2, 3])
s1.add(4)
print(s1)           # {1, 2, 3, 4}
```

### 2. 값 여러 개 추가하기(`update`)

```py
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)           # {1, 2, 3, 4, 5, 6}
```

### 3. 특정 값 제거하기(`remove`)

```py
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)           # {1, 3}
```

<br/>

---
## :three:&ensp; 교집합, 합집합, 차집합 구하기

```py
s1 = set([1, 2, 3, 4, 5, 6])    # {1, 2, 3, 4, 5, 6}
s2 = set([4, 5, 6, 7, 8, 9])    #          {4, 5, 6, 7, 8, 9}
```

### 1. 교집합

```py
s3 = s1 & s2                # `&` 기호 활용
s4 = s1.intersection(s2)    # `intersection()` 활용

print(s3)                   # {4, 5, 6}
print(s4)                   # {4, 5, 6}
```

### 2. 합집합

```py
s3 = s1 | s2                # `|` 기호 활용
s4 = s1.union(s2)           # `union()` 활용

print(s3)                   # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s4)                   # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### 3. 차집합

```py
s3 = s1 - s2                # `-` 기호 활용
s4 = s2 - s1                # `-` 기호 활용
print(s3)                   # {1, 2, 3}
print(s4)                   # {8, 9 ,7}

s5 = s1.difference(s2)      # `difference()` 활용
s6 = s2.difference(s1)      # `difference()` 활용
print(s5)                   # {1, 2, 3}
print(s6)                   # {8, 9 ,7}
```

<br/>

---
## :four:&ensp; set 자료형의 시간복잡도

|Operation|Average Case|Worst Case|
|-|:-:|:-:|
|`x in s`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|`Union s\|t`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(len(s)%2Blen(t))" />|-|
|`Insersection s&t`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(min(len(s)%2C%5C%20len(t)))" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(len(s)%5C%20%5Ctimes%5C%20len(t))" /> |
|`Multiple Intersection`<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=s_1%5C%20%26%5C%20s_2%5C%20%26%5C%20...%5C%20%26%5C%20s_n" />|-|<img src="https://chart.apis.google.com/chart?cht=tx&chl=(n-1)%5C%20%5Ctimes%5C%20O(l)" /><br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=l%5C%20%3D%5C%20max(len(s_1)%2C%5C%20...%2C%5C%20len(s_n))" />|
|`Difference s-t`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(len(s))" />|-|
|`s.difference_update(t)`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(len(t))" />|-|
|`Symmetric Difference s^t`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(len(s))" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(len(s)%5C%20%5Ctimes%5C%20len(t))" />|
|`s.symmetric_`<br/>`difference_update(t)`|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(len(t))" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(len(t)%5C%20%5Ctimes%5C%20len(s))" />|

* `difference s-t`이나 `s.difference(t)`의 연산은 worst case에 대해 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(len(s))" />의 시간 복잡도를 가짐. 이는 `s`의 모든 요소에 대해 `t`가 없는 경우, 새 집합에 추가하는 방식으로 구현되어 있기 떄문([source code: `set_difference()`](https://github.com/python/cpython/blob/master/Objects/setobject.c)).

* 한편, `s.difference_update(t)` 연산은 worst case에 대해 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(len(t))" />의 시간 복잡도를 가짐. 이는 `t`의 모든 요소에 대해 `s`에서 제거하는 방식으로 구현되었기 때문([source code: `set_difference_update_internal()`](https://github.com/python/cpython/blob/master/Objects/setobject.c)).

* `s-t`와 같은 집합 연산을 수행하려면 `s`와 `t`가 모두 집합이어야 함. 그러나 `t`가 반복 가능한 경우에도 동일한 방법을 수행할 수 있음(예: `s.difference(l)`, 여기서 `l`은 목록임).


<br/>

---
## Reference

* https://wikidocs.net/1015

* https://wiki.python.org/moin/TimeComplexity