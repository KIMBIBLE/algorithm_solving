# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; Python `set` 자료형

Python은 집합에 관한 연산을 처리하는 기능을 내장 자료형인 `set`을 통해 제공한다.

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

<br/>

---
## Reference

* https://wikidocs.net/1015

* https://wiki.python.org/moin/TimeComplexity