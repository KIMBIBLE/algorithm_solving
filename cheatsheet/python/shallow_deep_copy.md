# Assignment(`=`), Shallow Copy, Deep Copy

Python 에서 객체를 복사하는 방법은 크게 3가지(assignment operator, shallow copy, deep copy)방법이 있음.  

<br/>

|Type|code|Description|
|-|-|-|
|assignment(`=`)|`a = list`|변수에 객체의 레퍼런스를 복사함.|
|shallow copy|`s = list[:]`|변수에 새롭게 객체를 할당하여, 기존 객체의 내용을 복사함.|
|deep copy|`d = copy.deepcopy(list)`|변수에 새롭게 객체를 할당하여, 기존 객체의 내용을 recursive하게 복사함.|

<br/>

Mutable Object인 `list 자료형을 복사하는 방식`을 통해, 할당 연산자(`=`), Shallow Copy, Deep Copy의 차이에 대해 알아보자.

<br/>

:bulb:&ensp; 참고

> shallow copy와 deep copy의 차이는 compound object(list of list, class 인스턴스)의 복사 시에만 나타남!

<br/>

---
## :one:&ensp; assignment(`=`) 연산자

assignment 연산자는 copy를 하는 것이 아니기 때문에 새로운 객체가 생성되는 것이 아님! 새로운 변수로 해당 개체를 참조하는 것 뿐!

```py
x = [1, 2, 3]
y = x
hex(id(x)) == hex(id(y))    # True(0x10489fbc0)
```

<br/>

---
## :two:&ensp; shallow copy

Mutable element에 대한 `shallow copy`는 원본 element를 참조하는 상태! 

따라서 `nested list` 생성 시, shallow copy를 사용하게 되면 다음과 같은 형태로 복사가 수행됨

```txt
1. 새로운 compound object 생성.

2. 가능한 원본에 있는 객체에 대한 참조를 새롭게 생성된 compound object에 삽입.
```

<br/>

### 예시 1: Shallow Copy

```py
a = [[1, 2], [3, 4]
b = a[:] # shallow copy

b.append([3, 6])
print(b) # [[1, 2], [3, 4], [5, 6]]
print(a) # [[1, 2], [3, 4]]
```

<br/>

### 예시 2: Shallow Copy

원본이 compound object이라면, shallow copy 수행 시 새로운 object의 element를 원본 element의 레퍼런스 형태가 됨

```py
a = [[1, 2], [3, 4]]
b = a[:] # shallow copy
b[0].append(3)
print(b) # [[1, 2, 3], [3, 4]]
print(a) # [[1, 2, 3], [3, 4]]
```

<br/>

---
## :three:&ensp; deep copy

Mutable element에 대한 `deep copy`는 원본 element를 참조하는 상태가 아님!(별개의 복사본)

따라서 deep copy는 다음과 같은 과정을 통해 수행됨.

```txt
1. 새로운 compound object를 만듦.

2. 재귀적으로 원본 객체 내의 mutable object에 대한 object를 생성함. (재귀적으로 object 생성하는 이유는 compound object와 같은 경우 또한 복사가 수행될 수 있도록 하기 위함.)

3. 이후, 새롭게 생성된 object에 원본의 값을 복사해서 넣어줌!
```

<br/>

### Deep Copy의 예시

```py
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(3)
print(b) # [[1, 2, 3], [3, 4]]
print(a) # [[1, 2], [3, 4]]
```

<br/>

### examining the pointer locations

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

---
## :four:&ensp; `assignment(=)`, `shallow-copy`, `deep-copy`를 어느 상황에 사용할까?

### 1. list of integers: `[1, 2, 3]`
  
* assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)

* shallow-copy( `original[:]` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)

<br/>

### 2. compound objects: `[[1, 2], 3]`
  
  * assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)
  
  * deep-copy( `copy.deepcopy(original)` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)
nts)

<br/>

---
## 참고

- https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86