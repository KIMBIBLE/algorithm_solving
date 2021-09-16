# recursion limit 설정

## :one:&ensp; 파이썬 인터프리터의 재귀 깊이(default): `1000`

```py
import sys
sys.getrecursionlimit() # 1000
```

<br/>

## :two:&ensp; 파이썬 인터프리터의 재귀 깊이 재 설정

```py
import sys
limit = 2000
sys.setrecursionlimit(limit)
```
