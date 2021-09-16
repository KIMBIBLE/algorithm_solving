# Mutable, Immutable

파이썬의 객체에는 Mutable, Immutable 객체가 있음

- `Mutable Object`: 변경 가능한 객체(변경 가능한 객체)는 생성 후, 수정할 수 있는 객체를 말함.

- `Immutable Object`: 불변 객체(unchangeable 객체)는 생성된 후, 상태를 수정할 수 없는 객체를 말함.

<br/>

||Data Type|
|-|-|
|Mutable|`list`, `set`, `dict`|
|Immutable|`bool`, `int`, `float`, `tuple`, `str`, `frozenset`, `user defined class`|

<br/>

---

## :one:&ensp; Immutable 객체

Immutable Object는 생성후 객체 내용의 변경이 `불가능`함. 다음의 `int` 자료형에 대한 계산 예제를 보면, Immutable Object가 객체 생성 후 변경되는 방식으로 코드가 실행되는 것이 아니라, Immutable Object에 대한 계산 결과에 해당하는 Immutable Object의 주소값을 리턴하는 방식으로 코드가 실행되는 것을 확인할 수 있음.

```py
# x, y는 객체 내부의 값이 1인 int 형 immutable 객체를 가리킴.
x = 1     # x ------+
          #         +-> 1 (immutable object) : 0x10e161af0
y = x     # y ------+

hex(id(x)) # 0x10e161af0
hex(id(1)) # 0x10e161af0
hex(id(2)) # 0x10462db10
hex(id(3)) # 0x10462db30
```

<br/>

`1 + 2` 연산의 결과값이 현재 변수 x가 가리키는 Immutable int 자료형 "1"(0x10e161af0)에 저장되는 것이 아니라, 계산된 결과 값에 해당되는 Immutable int 자료형 "3"(0x10462db30)을 가리키게 됨.

```py
y += 2    # y --------> 3 (immutable) : 0x10e161b30

hex(id(x)) # 0x10e161af0: x가 레퍼런스하는 메모리의 값이 바뀐 것이 아니라, y는 새로운 메모리를 가리키게 됨!
hex(id(y)) == hex(id(3))    # True(0x10e161b30)
hex(id(1+2)) == hex(id(3))  # True(0x10e161b30)
```

<br/>

----
## :two:&ensp; Mutable 객체

Mutable Object는 다음의 `list` 예제과 같이 생성 후 변경이 가능함.

```py
x = [1, 2, 3]
y = x

x.append(4) # 생성된 Immutable Object인 list의 내용을 수정.
id(x) == id(y)  # True(0x10489fb40)
```