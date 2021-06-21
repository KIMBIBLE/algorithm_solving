# 1차원 배열의 주요 `메서드`와 `특징`: List

> 파이썬에서 일차원 배열을 표현할 수 있는 방법은 다양하지만, 해당 문서는 가장 대표적인 방법인 `List`를 활용한 방법에 대해 다룹니다.

## :one:&ensp; 1차원 배열의 주요 메서드

### 1. 선언

```py
a = []
a = list()
a = [] * 10     # []을 리턴하는 것에 주의!!!!!! 
a = [0] * 10    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [[]] * 10   # [[], [], [], [], [], [], [], [], [], []]
```

<br/>

### 2. 데이터 추가

```py
a.append(1)     # [1]
a.append(2)     # [1, 2]

b = a * 3       # [1, 2, 1, 2, 1, 2]
c = [3]
a + c           # [1, 2, 3]
```

<br/>

### 3. 슬라이싱

```py
a = [1, 2, 3, 4, 5]
b = a[0:2]              # [1, 2] 리스트를 새로 생성하여 반환
```

<br/>


---

## :two: 1차원 배열의 주요 특징

### 1. Mutable Object인 Python List

> 파이썬의 List는 대표적인 `Mutable Object`! 따라서 파이썬에서 mutable object를 쓸 때는 이거 주의해야 함! 


```py
a = [1, 2, 3]
b = a               # b = [1, 2, 3]
id(a) == id(b)      # True

a.append(4)
print(b)            # [1, 2, 3, 4]

b.append(5)
print(a)            # [1, 2, 3, 4, 5]
```

* 변수 a, b가 동일한 `mutable object`를 가리키는 레퍼런스이기 때문에 위와 같은 현상이 발생함.

<br/>

### 2. 복사 (Assign Operator `'='` VS Shallow Copy)

:point_right:&ensp; 1차원 리스트의 Shallow Copy Examples

```py
a = [1, 2, 3]   # mutable object 'a'
b = a           # assign `a` to `b`
c = a.copy()    # shallow copying `a` to `c`

a is b          # True
a is c          # False
a == c          # True
```

<table>
<thead>
<tr>
    <th>연산자 및 메서드</th>
    <th>내용</th>
</tr>
</thead>

<tbody>
<tr>
    <td><code>=  연산자</code></td>
    <td>객체의 메모리 주소를 대상 변수에 그대로 복사함.</td>
</tr>
<tr>
    <td rowspan="2"><code>copy()</code></td>
    <td>객체의 내용을 복사함(<code>shallow copy</code>). 이 때 리스트 요소들의 값이 그대로 새로운 객체로 복사됨. </td>
</tr>
<tr>
    <td>1차원 배열의 경우 <code>deep copy</code>를 고려할 필요는 없음. 이는 파이썬에서 다른 객체를 포함하는 <code>복합 객체(compound object)</code>가 아니라면, <code>shallow copy</code>와 <code>deep copy</code>간에 차이가 없기 때문.</td>
</tr>
<tr>
    <td><code>== 연산자</code></td>
    <td>두 객체의 content와 value가 동일한지?</td>
</tr>
<tr>
    <td><code>is 연산자</code></td>
    <td>두 객체가 동일한 객체인지?</td>
</tr>

</tbody>
</table>

<br/>

:point_right:&ensp; 함수 인자 전달 시, 어떤 형태의 복사가 수행될까?

> 아래의 테스트 코드를 실행해보면, 함수의 전달인자와 매개변수가 `= 연산자`의 결과와 같이 `동일한 메모리 주소`를 가리키는 것을 확인할 수 있음.

```python
def test(x):
    print(hex(id(x)))   # 0x104a1f3c0

a = [1, 2, 3]
print(hex(id(a)))       # 0x104a1f3c0
test(a)
```