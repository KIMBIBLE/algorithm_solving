# Sorting in Programming Languages

## Table of Contents

1. [Python](#h2-1)

<br/>

---

<h2 id="h2-1"> 1️⃣&ensp; Python</h2>

### 1. `data.sort()` vs `sorted(data)`

```py
a = [ 1, 5, 3, 4, 9, 2]
b = sorted(a)   # 기존 리스트를 변경하지 않고 새로운 리스트 반환
a.sort()        # 리스트를 정렬된 상태로 변경
```

<br/>

### 2. Sorting Reverse Order

```py
c = a.sort(reverse=True)
d = [ [1, 4], [3, 5], [0, 6], [0, 4], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [5, 7], [12, 14] ]
```

<br/>

### 3. Sorting with Key(With lamba & Without lambda)

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

<br/>

### 4. Sorting Dictionary

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
