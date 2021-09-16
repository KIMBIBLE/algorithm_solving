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

Mutable element에 대한 `shallow copy`는 원본 element를 참조하는 상태!  따라서 `nested list` 생성 시, shallow copy를 사용하게 되면 다음과 같은 형태로 복사가 수행됨.

a. 새로운 compound object 생성.

b. 원본에 있는 `객체에 대한 참조`를 새롭게 생성된 compound object에 삽입.


<br/>

### 1. Shallow Copy를 통한 객체 복사 방법

```py
a = [[1, 2], [3, 4]] # compound object: nested list
b = a[:] # shallow copy

# compound object를 shallow copy하면, 원본 객체의 크기만큼 객체가 새롭게 할당됨.
hex(id(a)) == hex(id(b)) # False(0x1048a93c0 != 0x1048a9280)
sys.getsizeof(a) == sys.getsizeof(b) # True(72 == 72)

# compound object를 shallow copy하면, 원본에 있는 `객체에 대한 참조`가 새롭게 생성된 compound object에 삽입됨. 따라서 객체의 내용이 동일한 것을 확인 가능.
print(a) # [[1, 2], [3, 4]]
print(b) # [[1, 2], [3, 4]]

# shallow copy된 객체는 새롭게 할당되었기 때문에, 해당 객체에 데이터를 추가하면 원본 객체에 영향을 미치지 않음.
b.append([5, 6])
print(b) # [[1, 2], [3, 4], [5, 6]]
print(a) # [[1, 2], [3, 4]]
```

<br/>

### 2. Shallow Copy를 통해 Compound Object를 복사할 때 주의사항

원본이 compound object이라면, shallow copy 수행 시 새로운 object의 element는 원본 element의 레퍼런스와 동일함. 

<br/>

:bulb:&ensp; shallow copy된 compound object 내부의 mutable/immutable 객체를 수정하는 작업이 원본 데이터에 미치는 영향.

*  `mutable object를 수정`: 원본 데이터에도 영향을 미침.

* `immutable object를 수정`: 원본 데이터에 영향을 미치지 않음.(immutable 객체는 할당 이후 수정이 불가능하기 때문에, 데이터 변경 코드가 실제로 객체 내의 데이터를 변경하는 것이 아니라 참조만 변경하는 것이기 때문.)

```py
# 1. compound object 할당 & shallow copy
a = [[1, 2], [3, 4], 1] # compound object 할당
b = a[:] # shallow copy: 해당 객체 내의 값을 그대로 복사


# 2. compound object내의 mutable object의 데이터 수정
b[0].append(3) 
print(b) # [[1, 2, 3], [3, 4], 1]
print(a) # [[1, 2, 3], [3, 4], 1] -> 원본 데이터에도 영향을 미침

# shallow copy는 해당 객체 내의 값을 그대로 복사하기 때문에 compound object 같은 경우, 객체의 데이터(주소값)가 그대로 복사 됨. 
hex(id(a[0])) == hex(id(b[0])) # True(0x1048a9280 == 0x1048a9280)


# 3. compound object내의 immutable object의 데이터 수정
b[2] = 2 
print(b) # [[1, 2], [3, 4], 2]
print(a) # [[1, 2], [3, 4], 1]

hex(id(a[2])) == hex(id(b[2])) # False(0x10462daf0 != 0x10462db10)
```

<br/>

---
## :three:&ensp; deep copy

Mutable element에 대한 `deep copy`를 수행하면, 새롭게 생성된 객체가 원본 element를 참조하는 상태가 아니라 별개의 복사본 형태로 존재하게 됨. deep copy는 다음과 같은 과정을 통해 수행됨.

a. 새로운 compound object를 만듦.

b. 재귀적으로 원본 객체 내의 mutable object에 대한 object를 생성함. (재귀적으로 object 생성하는 이유는 compound object 내의 mutable object 또한 참조 복사가 아니라 실제 데이터가 복사되도록 하기 위함.)

c. 이후, 새롭게 생성된 object에 원본의 값을 복사해서 넣어줌!

<br/>

### 1. Deep Copy의 예시: `copy.deepcopy()`

```py
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(3)
print(b) # [[1, 2, 3], [3, 4]]
print(a) # [[1, 2], [3, 4]]
```

<br/>

---
## :four:&ensp; Examining the pointer locations:<br/> assignment operator(`=`) vs shallow copy vs deep copy

```py
# Copy compound object with assignment operator
original = [1, [2, 3]]
a = original # assignment
id(a) == id(original) # True (Same Pointer)


# Copy compound object with shallow copy
s = original[:] # shallow-copy
id(s) == id(original) # False: s has own pointer
id(s[0]) == id(original[0]) # True
id(s[1]) == id(original[1]) # True: s[1]은 original[1]의 레퍼런스!


# Copy compound object with deep copy
import copy
d = copy.deepcopy(original)
id(d) == id(original) # False
id(d[0]) == id(original[0]) # True
id(d[1]) == id(original[1]) # False: deep-copy를 통해 새로운 객체가 생성되고, 생성된 객체에 original[1]의 값이 복사된 것!
```

<br/>

---
## :five:&ensp; `assignment(=)`, `shallow-copy`, `deep-copy`를 어느 상황에 사용할까?

### 1. list of immutable object: `[1, 2, 3]`
  
* assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)

* shallow-copy( `original[:]` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)

<br/>

### 2. compound objects: `[[1, 2], 3]`
  
  * assignment( `=` ) 사용: 새로운 참조를 통해 original list의 변화를 주고 싶을 때!(e.g. call by reference로 함수 전달)

  * shallow copy(`dst = src[:]`): 권장하지 않음.

  * deep-copy( `copy.deepcopy(original)` ) 사용: 새로운 참조를 객체의 값만 읽을 때 사용하고, 객체 내부를 변경하고 싶지 않을 때!(e.g. call by value로 함수 전달)
nts)

<br/>

---
## 참고

- https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86