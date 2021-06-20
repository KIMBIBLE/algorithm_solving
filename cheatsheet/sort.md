# Sort

## :one:&nbsp; 코딩테스트 정렬 문제 유형

### 1. 내장 정렬 라이브러리를 사용하는 문제

> 해당 문제 해결을 위해 데이터를 정렬이 필요한 경우. 문제를 분석해서 `"정렬을 수행했을 때 쉽게 문제가 풀리겠구나" 라는 생각`을 떠올리는 것이 중요한 유형. 정렬 라이브러리의 사용 기법에 대해 알고 있어야 함.

<details><summary>대표적인 문제</summary>

</details><br/>


### 2. 정렬 알고리즘의 원리를 물어보는 문제

> 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고있어야 함.

<details><summary>대표적인 문제</summary>

</details><br/>

### 3. 더 빠른 정렬이 필요한 문제

> 퀵 정렬 방식으로 해결이 불가능하며, 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나, 기존 알고리즘의 구조를 문제에 적합하게 개선하는 작업이 필요함.

<details><summary>대표적인 문제</summary>

</details><br/>


---
## :two:&nbsp; Programming Languages

### 1. Python

<details><summary>data.sort() vs sorted(data)</summary>

```py
a = [ 1, 5, 3, 4, 9, 2]
b = sorted(a)   # 기존 리스트를 변경하지 않고 새로운 리스트 반환
a.sort()        # 리스트를 정렬된 상태로 변경
```
</details>

<details><summary>Sorting Reverse Order</summary>

```py
c = a.sort(reverse=True)
d = [ [1, 4], [3, 5], [0, 6], [0, 4], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [5, 7], [12, 14] ]
```
</details>


<details><summary>Sorting with Key(With lamba & Without lambda)</summary>

```py
d = [ [1, 4], [3, 5], [0, 6], [0, 4], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [5, 7], [12, 14] ]

e = sorted(d, key = lambda x : (x[0], x[1])) 
# x[0]를 기준으로 정렬 -> x[1]를 기준으로 정렬
# [[0, 4], [0, 6], [1, 4], [3, 5], [3, 8], [5, 7], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]

f = sorted(d, key = lambda x : (x[1], x[0])) 
# x[1]를 기준으로 정렬 -> x[0]를 기준으로 정렬
# [[0, 4], [1, 4], [3, 5], [0, 6], [5, 7], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]

def setting(data):
    return (data[0], data[1])

sorted(d, key = setting)
# [[0, 4], [0, 6], [1, 4], [3, 5], [3, 8], [5, 7], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
```
</details>


<details><summary>Sorting Dictionary</summary>

```py
dicts = [
    {"idx": 3, "data": "asdf"},
    {"idx": 1, "data": "qwer"},
    {"idx": 2, "data": "hjkl"},
    {"idx": 4, "data": "zxcv"}
    ]
def setting(data):
    return data["idx"]

sorted(dicts, key = setting)
# [{'idx': 1, 'data': 'qwer'}, {'idx': 2, 'data': 'hjkl'}, {'idx': 3, 'data': 'asdf'}, {'idx': 4, 'data': 'zxcv'}]

sorted(dicts, key = lambda x: x["idx"])
# [{'idx': 1, 'data': 'qwer'}, {'idx': 2, 'data': 'hjkl'}, {'idx': 3, 'data': 'asdf'}, {'idx': 4, 'data': 'zxcv'}]
```
</details>

<br/>

---
## :three:&nbsp; Sorting 알고리즘

* [소팅 알고리즘 종류 / 구현 / 시간복잡도 / 공간복잡도 정리 및 비교 분석](../dongbin_book/chap5_sort/README.md)