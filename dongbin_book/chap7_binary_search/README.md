# 배열 자료형에 대한 이진탐색

## :one:&ensp; 배열 이진탐색

> 코딩테스트에서 이진 탐색 알고리즘을 사용하는 경우는 탐색의 범위가 매우 큰 경우가 대다수임. 만약 탐색의 범위가 1,000만 이상인 경우 이진탐색과 같이 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog%7B%7D%7Bn%7D)" /> 복잡도의 알고리즘을 활용해야 함.

<br/>

### :bulb:&ensp; 아이디어

> 배열을 대상으로 하는 이진탐색은 `배열 내부의 데이터가 이미 정렬이 되어 있어야만 사용 가능함`. 이진탐색 알고리즘은 탐색을 위해, 위치를 나타내는 3가지 주요 변수를 사용함. 찾고자 하는 데이터와 중간점을 반복적으로 비교해서, 목표 데이터를 찾는 것이 배열 이진 탐색에 주된 아이디어. 한번 확인할 때 마다 확인하고자 하는 원소의 갯수가 절반씩 줄어들기 때문에 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(%5Clog%7B%7D%7Bn%7D)" />의 시간 복잡도를 가짐.

* 시작점: 탐색하고자 하는 범위의 시작점.

* 끝점: 탐색하고자 하는 범위의 끝점.

* 중간점: 탐색하고자 하는 범위의 중간점.

<br/>

---
## :two:&ensp; 프로그래밍 언어별 배열 이진탐색 구현

### 1. Python

<details><summary>입출력 데이터</summary>

```bash
# Input Data 1 
7
1 3 5 7 9 11 13 15 17 19

# Output 1
4


# Input Data 2
7
1 3 5 6 9 11 13 15 17 19

# Output 2
Cannot find 7 in list
```

</details><br/>


:point_right:&ensp; 재귀함수를 통한 구현

```python
import sys
readline = lambda: sys.stdin.readline().rstrip()

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)


if __name__ == '__main__':
    target = int(readline())
    array = list(map(int, readline().split()))

    result = binary_search(array, target, 0, len(array) - 1)
    if result == None:
        print('Cannot find {} in list'.format(target))
    else:
        print(result + 1)
```

<br/>

:point_right:&ensp; 반복문을 통한 구현

```py
import sys
readline = lambda: sys.stdin.readline().rstrip()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


if __name__ == '__main__':
    target = int(readline())
    array = list(map(int, readline().split()))

    result = binary_search(array, target, 0, len(array) - 1)
    if result == None:
        print('Cannot find {} in list'.format(target))
    else:
        print(result + 1)
```