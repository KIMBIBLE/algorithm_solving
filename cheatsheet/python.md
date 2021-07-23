# Python Cheat Sheet

## Table of Contents

1. [Mutable, Immutable](#h2-1)

2. [Shallow Copy, Deep Copy](#h2-2)

3. [recursion limit](#h2-3)

4. [use string as function name](#h2-4)

5. [Error Case](#h2-5)

<br/>

---

<h2 id="h2-1">1. Mutable, Immutable</h2>

파이썬의 객체에는 Mutable, Immutable 객체가 있음

|Mutable|Immutable|
|:-:    |:-:      |
|`list`, `set`, `dict`|`bool`, `int`, `float`, `tuple`, `str`, `frozenset`, `user defined class`|

```py
x = 1     x ------+
                  +-> 1 (immutable) : 0x10e161af0
y = x     y ------+

hex(id(x)) # 0x10e161af0
hex(id(1)) # 0x10e161af0

y += 2    y --------> 3 (immutable) : 0x10e161b30

hex(id(x)) # 0x10e161af0: x가 레퍼런스하는 메모리의 값이 바뀐 것이 아니라, y는 새로운 메모리를 가리키게 됨!
hex(id(y)) # 0x10e161b30
hex(id(3)) # 0x10e161b30
```

<br/>

[Top](#table-of-contents)

---
<h2 id="h2-2">2. Shallow Copy, Deep Copy <a href="https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86">(Link)</a></h2>

shallow copy와 deep copy의 차이는 compound object(list of list, class 인스턴스)의 복사 시에만 나타남!

<br/>

:bulb:&ensp; list 복사 방법의 예시 ( `original -> list`)를 살펴보자!

> Python 에서 List를 복사하는 방법은 크게 3가지(assignment operator, shallow copy, deep copy)방법이 있음.

### 1. assignment( `a = list` )
  
copy를 하는 것이 아니기 때문에 새로운 객체가 생성되는 것이 아님! 새로운 변수로 해당 개체를 참조하는 것 뿐!
  
<br/>

### 2. shallow copy( `s = list[:]` )

Mutable element에 대한 `shallow copy`는 원본 element를 참조하는 상태! 

따라서 `nested list` 생성 시, shallow copy를 사용하게 되면 다음과 같은 형태로 복사가 수행됨

```txt
1. 새로운 compound object 생성.

2. 가능한 원본에 있는 객체에 대한 참조를 새롭게 생성된 compound object에 삽입.
```

* Shallow Copy 예시 1

  ```py
  a = [[1, 2], [3, 4]
  b = a[:] # shallow copy

  b.append([3, 6])
  print(b) # [[1, 2], [3, 4], [5, 6]]
  print(a) # [[1, 2], [3, 4]]
  ```

* Shallow Copy 예시 2

  원본이 compound object이라면, shallow copy 수행 시 새로운 object의 element를 원본 element의 레퍼런스 형태가 됨

  ```py
  a = [[1, 2], [3, 4]]
  b = a[:] # shallow copy
  b[0].append(3)
  print(b) # [[1, 2, 3], [3, 4]]
  print(a) # [[1, 2, 3], [3, 4]]
  ```

<br/>

### 3. deep copy( `d = copy.deepcopy(list)` )
    
Mutable element에 대한 `deep copy`는 원본 element를 참조하는 상태가 아님!(별개의 복사본)

따라서 deep copy는 다음과 같은 과정을 통해 수행됨.

```txt
1. 새로운 compound object를 만듦.

2. 재귀적으로 원본 객체 내의 mutable object에 대한 object를 생성함. (재귀적으로 object 생성하는 이유는 compound object와 같은 경우 또한 복사가 수행될 수 있도록 하기 위함.)

3. 이후, 새롭게 생성된 object에 원본의 값을 복사해서 넣어줌!
```

* Deep Copy의 예시

  ```py
  import copy
  a = [[1, 2], [3, 4]]
  b = copy.deepcopy(a)
  b[0].append(3)
  print(b) # [[1, 2, 3], [3, 4]]
  print(a) # [[1, 2], [3, 4]]
  ```

* examining the pointer locations

  ```py
  original = [1, [2, 3]]
  a = original # assignment
  id(a) == id(original) # True (Same Pointer)

  s = original[:] # shallow-copy
  id(s) == id(original) # False: s has own pointer
  id(s[0]) == id(original[0]) # True
  id(s[1]) == id(original[1]) # True: s[1]은 original[1]의 레퍼런스!

  import copy
  d = copy.deepcopy(original)
  id(d) == id(original) # False
  id(d[0]) == id(original[0]) # True
  id(d[1]) == id(original[1]) # False: deep-copy를 통해 새로운 객체가 생성되고, 생성된 객체에 original[1]의 값이 복사된 것!
  ```

<br/>

### :bulb:&ensp; `assignment(=)`, `shallow-copy`, `deep-copy`를 어느 상황에 사용할까?

* list of integers: `[1, 2, 3]`
  
  * assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)
  
  * shallow-copy( `original[:]` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)

* compound objects: `[[1, 2], 3]`
  
  * assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)
  
  * deep-copy( `copy.deepcopy(original)` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)

<br/>

[Top](#table-of-contents)

---
<h2 id="h2-3">3. recursion limit</h2>

* 파이썬 인터프리터의 재귀 깊이(default): 1000
  ```py
  import sys
  sys.getrecursionlimit() # 1000
  ```

* 파이썬 인터프리터의 재귀 깊이 재 설정
  ```py
  limit = 2000
  sys.setrecursionlimit(limit)
  ```

<br/>

[Top](#table-of-contents)

---
<h2 id="h2-4">4. use string as function name</h2>

```py
func = getattr(class_name, string_type_function_name)
func()
```

<br/>

[Top](#table-of-contents)

---
<h2 id="h2-5">5. Error Case</h2>

* `TypeError: '---' object is not callable` 에러
  
    이와 같은 에러는 str, list 등의 변수명을 파이썬의 내장 함수명과 겹치게 네이밍할 때 자주 발생!


[Top](#table-of-contents)