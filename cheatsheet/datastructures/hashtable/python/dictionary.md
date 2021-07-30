# <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/KIMBIBLE/KIMBIBLE/main/icons/python.svg" title="Python" width="22px"/></a>&ensp; Python `Dictionary` 자료형

Python은 `dictionary` 자료형을 통해 해시 테이블을 만들 수 있다.

dictionary은 `immutable한 키(key)`와 `mutable한 값(value)`으로 `맵핑되어 있는 순서가 없는 집합`.

<br/>

## Table of Contents

* [Dictionary 생성](#section_01)
* [Dictionary 요소 추가/수정](#section_02)
* [Dictionary의 요소 검색](#section_03)
* [Dictionary의 요소 삭제](#section_04)
* [Dictionary의 요소 복사](#section_05)
* [Python dictionary operation의 Time Complexity](#section_06)


<br/>

---

<!--
################### Section 01 #############################
-->
<h2 id="section_01">1️⃣&ensp; Dictionary 생성</h2>


### 1. dictionary(딕셔너리) 선언

<details>
<summary><b>dictionary 생성: Expression(<code>{key: value}</code>)</b></summary>

```py
dict_1 = {}
dict_2 = {'name':'bbkim', 'birth': '1207'}
dict_3 = {'a': 1, 'b': [1, 2, 3]}
```

> :bulb:&ensp; dictionary의 키로는 immutable한 값은 사용할 수 있지만, mutable한 객체는 사용할 수 없음.

* `Immutable` : 숫자(number), 문자열(string), 튜플(tuple)

* `Mutable` : 리스트(list), 딕셔너리(dictionary), NumPy의 배열(ndarray)

---

</details>

<details>
<summary><b>dictionary 생성: 생성자(<code>dict()</code>)</b></summary>

```py
# dict constructor를 통핸 dictionary 생성.
dict_3 = dict(a = 1, b = 2, c= 3, d = 4)
```

---

</details>

<details>
<summary><b>dictionary 생성: 다른 자료형(list, tuple)으로부터의 변환</b></summary>

```py
dict_4 = dict([['bbkim', 123], ['awesome', 345]])
dict_5 = dict([('bbkim', 123), ('awesome', 345)])

# {'bbkim': 123, 'awesome': 345}
```

> :bulb:&ensp; 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있음. 

---

</details>

<details>
<summary><b>딕셔너리 만들 때 주의할 사항: 키가 중복되는 경우</b></summary>

```py
a = {1:'a', 1:'b'} # {1: 'b'} 
```

> :bulb:&ensp; 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨!

</details>

<br/>

---

<!--
################### Section 02 #############################
-->
<h2 id="section_02">2️⃣&ensp; Dictionary 요소 추가/수정</h2>

<details>
<summary><b>dictionary 요소 추가/수정 (단일): <code>dict_variable[] = val</code></b></summary>

```py
a = {1: ['a', 'b', 'c'], 2: ['q', 'w', 'e']}

# dictionary에 요소 추가(단일)
a[3] = ['h'] # {1: ['a', 'b', 'c'], 2: ['q', 'w', 'e'], 3: ['h']}

# dictionary의 요소 수정(단일)
a[1] = 1 # {1: 1, 2: ['q', 'w', 'e'], 3: ['h']}
```

---

</details>

<details>
<summary><b>dictionary 요소 추가/수정 (단일 or 여러개): <code>update()</code></b></summary>

```py
a = {1: ['a', 'b', 'c'], 2: ['q', 'w', 'e']}

# dictionary에 요소 추가(단일 or 여러개)
a.update({1: 'a', 2: 'b'}) # {1: 'a', 2: 'b'}

# dictionary의 요소 수정(단일 or 여러개)
a.update({3: 3, 4: 4}) # {1: 'a', 2: 'b', 3: 3, 4: 4}
```

</details><br/>

---
<!--
################### Section 03 #############################
-->
<h2 id="section_03">3️⃣&ensp; Dictionary의 요소 검색</h2>


<details>
<summary><b>Key 리스트 만들기: <code>keys()</code></b></summary>

```py
x = dict(a = 1, b = 2, c = 3, d = 4)
x.keys() # dict_keys(['a', 'b', 'c', 'd'])
type(x.keys()) # <class 'dict_keys'>
```

> :bulb:&ensp; `x.keys()` 실행 시 iterable한 `dict_keys` 객체가 반환됨. (key들의 순서는 보장하지 않음!)

---

</details>

<details>
<summary><b>Value 리스트 만들기: <code>values()</code></b></summary>

```py
x = dict(a = 1, b = 2, c = 3, d = 4)
x.values() # dict_values([1, 2, 3, 4])
type(x.keys()) # <class 'dict_values'>
```

> :bulb:&ensp; `x.values()` 실행 시 iterable한 `dict_values` 객체가 반환됨. (value들의 순서는 보장하지 않음!)

---

</details>

<details>
<summary><b>Key, Value 쌍 얻기: <code>items()</code></b></summary>

```py
x = dict(a = 1, b = 2, c = 3, d = 4)
x.items() # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
type(x.items()) # <class 'dict_items'>

for k, v in x.items():
    print("key = {key}, value={value}".format(key=k, value=v))
"""
key = a, value=1
key = b, value=2
key = c, value=3
key = d, value=4
"""
```

> :bulb:&ensp; `x.items()` 실행 시 iterable한 `dict_items` 객체가 반환됨. (item들의 순서는 보장하지 않음!)

---

</details>

<details>
<summary><b>Key로 Value얻기: <code>dict_variable[]</code>, <code>get()</code></b></summary>

```py
# dict_variable['key_name'] syntax를 통한 value 접근

x = dict(a = 1, b = 2, c = 3, d = 4)
x['a'] # 1
x['asdf'] # 존재하지 않는 키로 접근 시 KeyError Exception 발생
"""
raceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'asdf'
"""
```

```py
# dict_variable.get('key_name') syntax를 통한 value 접근

x = dict(a = 1, b = 2, c = 3, d = 4)
x.get('a') # 1
x.get('asdf') == None # True: 존재하지 않는 키로 접근 시 None 리턴
```

---

</details>

<details>
<summary><b>해당 Key가 딕셔너리 안에 있는지 조사하기: <code>in</code></b></summary>

```py
x = dict(a = 1, b = 2, c = 3, d = 4)
'a' in x # True
'asdf' in x # False
```
---

</details>

<details>
<summary><b>dictionary의 요소 출력: <code>pprint module</code></b></summary>

```py
from pprint import pprint

dict_1 = {'bbkim': 123, 'awesome': 345, 'qwer': [1, 2, 3, 4], 'age': 10, 'sdfg': ['a', 'b', 'c', 'd']}
pprint(a)

"""
{'age': 10,
 'awesome': 345,
 'bbkim': 123,
 'qwer': [1, 2, 3, 4],
 'sdfg': ['a', 'b', 'c', 'd']}
"""
```
</details><br/>

---

<!--
################### Section 04 #############################
-->
<h2 id="section_04">3️⃣&ensp; Dictionary의 요소 삭제</h2>

<details>
<summary><b>Key, Value 쌍 모두 지우기: <code>clear()</code></b></summary>

```py
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
x.clear()
print(a) # {}
```

---

</details>

<details>
<summary><b>Key, Value 쌍 지우기(단일): <code>del dict_variable</code></b></summary>

```py
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
del x['a']
print(a) # {'b': 20, 'c': 15, 'd': 30}
```

---

</details>

<details>
<summary><b>Key, Value 쌍 지우기(단일): <code>pop()</code></b></summary>

```py
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}

# 존재하는 키를 pop할 때
x.pop('a') # [1, 2, 3]
print(x) # {'b': 20, 'c': 15, 'd': 30}

# 존재하지 않는 키를 pop할 때 without parameter
x.pop('asdf') # KeyError Exception 발생
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'asdf'
"""

# 존재하지 않는 키를 pop할 때 with parameter
x.pop('asdf', None) == None # True
```

---

</details>

<details>
<summary><b>Key, Value 쌍 지우기(단일): <code>del</code> vs <code>pop()</code>의 성능 비교 및 권장하는 방식</b></summary>

```py
from timeit import timeit

del_snippet = "x1 = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}; del x1['a']"
pop_snippet = "x2 = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}; x2.pop('a', None)"

timeit(del_snippet) # 백만번 실행시간: 0.19542962400009856
timeit(pop_snippet) # 백만번 실행시간: 0.22955768899964824
```

> :bulb:&ensp; 평균적인 실행 시간은 `pop()`이 `del`보다 느림. 하지만 `pop()`은 `fallback 값`을 가지고 있어 런타임 오류 핸들링에 용이함.

</details><br/>

---

<!--
################### Section 05 #############################
-->
<h2 id="section_05">5️⃣&ensp; Dictionary의 요소 복사</h2>

<details>
<summary><b>dictionary의 shallow copy: <code>copy()</code></b></summary>

```py
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
y = x.copy() # shallow copy

# dictionary의 mutable element 수정
x['a'].append(4)
print(x) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
id(x) == id(y) # Fasle
id(x['a']) == id(y['a']) # True

# dictionary의 immutable element 수정
x['b'] = 3 
print(x) # {'a': [1, 2, 3, 4], 'b': 3, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
id(x) == id(y) # Fasle
id(x['b']) == id(y['b']) # False
```

> :bulb:&ensp; `copy()` 사용 시, 복사된 객체 저장을 위한 새로운 객체가 생성되지만, 내부의 mutable element의 경우 주소값만 복사됨.

---

</details>

<details>
<summary><b>dictionary의 shallow copy: assignment operator(<code>=</code>)</b></summary>

```py
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
y = x # shallow copy

# dictionary의 mutable element 수정
x['a'].append(4)
print(x) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
id(x) == id(y) # True
id(x['a']) == id(y['a']) # True

# dictionary의 immutable element 수정
x['b'] = 3 
print(x) # {'a': [1, 2, 3, 4], 'b': 3, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3, 4], 'b': 3, 'c': 15, 'd': 30}
id(x) == id(y) # True
id(x['b']) == id(y['b']) # True
```

> :bulb:&ensp; assignment operator(`=`) 사용 시, 새로운 객체가 생성되지 않고 변수의 참조만 복사됨. 따라서 두 변수가 같은 객체를 가리킴.

---

</details>

<details>
<summary><b>dictionary의 deep copy: <code>copy.deepcopy()</code></b></summary>

```py
import copy
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
y = copy.deepcopy(x)

# dictionary의 mutable element 수정
x['a'].append(4)
print(x) # {'a': [1, 2, 3, 4], 'b': 20, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
id(x) == id(y) # False
id(x['a']) == id(y['a']) # False

# dictionary의 immutable element 수정
x = {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
x['b'] = 3 
print(x) # {'a': [1, 2, 3], 'b': 3, 'c': 15, 'd': 30}
print(y) # {'a': [1, 2, 3], 'b': 20, 'c': 15, 'd': 30}
id(x) == id(y) # False
id(x['b']) == id(y['b']) # False
```

> :bulb:&ensp; `copy.deepcopy()` 사용 시, 복사된 객체 저장을 위한 새로운 객체가 생성되고, 내부의 mutable element들 또한 주소값만 복사되지 않고 내용까지 복사됨.

</details><br/>

---
<h2 id="section_06">6️⃣&ensp; Python dictionary operation의 Time Complexity</h2>

### 1. Assumptions

* dict의 Average Case 측정은 dict 객체에 대한 `해시 함수`가 충돌을 흔하지 않게 할 만큼 `충분히 강력하다고 가정`함.

* Average Case는 `매개변수에 사용된 키`가 모든 키 세트에서 `무작위로 균일하게 선택된다고 가정`합니다

* 실제로 `str 키`만 처리하는 dicts에 대한 fast-path가 있습니다. 이것은 알고리즘 복잡성에 영향을 미치지 않지만 일반적인 프로그램이 얼마나 빨리 완료되는지와 같은 상수 요소에 상당한 영향을 미칠 수 있음.

<br/>

### 2. Time Complexity

|Opeartion|Average Case|Amortized Worst Case|
|-|-|-|
|k in d|`O(1)`|`O(n)`|
|Copy|`O(n)`|`O(n)`|
|Get Item<sup>1</sup>|`O(1)`|`O(n)`|
|Set Item|`O(1)`|`O(n)`|
|Delete Item|`O(1)`|`O(n)`|
|Iteration<sup>2</sup>|`O(n)`|`O(n)`|

1. 이러한 작업은 "Amortized Wort Case"에서 "Amortized" 부분에 의존함. 개별 작업은 컨테이너의 history에 따라 놀라울 정도로 오래 걸릴 수 있음.

2. 이러한 작업의 경우 worst case의 n은 현재 크기가 아니라 컨테이너가 달성한 최대 크기를 말함. 예를 들어 N개의 개체가 dictionary에 추가되고 N-1개가 삭제되면, dictionary은 다른 삽입이 이루어질 때까지 (적어도) N개의 개체에 맞게 크기가 조정됨.

<br/>

---
## Reference

* https://wikidocs.net/16

* https://wikidocs.net/16043

* https://www.delftstack.com/ko/howto/python/how-to-remove-an-element-from-a-python-dictionary/

* https://wiki.python.org/moin/TimeComplexity