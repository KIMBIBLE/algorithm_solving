# Sort

[[뒤로](../../cheatsheet/sort.md)]

## :one:&nbsp; 소팅 알고리즘의 종류

### 1. 선택정렬(Selection Sort)

> 매번 가장 작은 것을 선택하는 방식으로 정렬을 수행하는 방식. 정렬되지 않은 상태의 리스트를 대상으로 최솟값 찾기를 반복함. 선택된 최솟값을 리스트의 시작 원소부터 순차적으로 교환하는 과정을 반복하는 동작을 통해 정렬이 수행됨.

<details><summary>Sample</summary>

```
# Original
7 5 9 0 3 1 6 2 4 8

# Sorting Setps
0 5 9 7 3 1 6 2 4 8     # 0 <-> 7 변경됨.
0 1 9 7 3 5 6 2 4 8     # 1 <-> 5 변경됨.
0 1 2 7 3 5 6 9 4 8     # 2 <-> 9 변경됨.

   +-------------------- Sorted 
   |  +----------------- 선택될 최솟값을 삽입할 위치
   |  |     +----------- 최솟값 탐색을 수행할 구간 
   |  |     |
   V  V     V
+===+ +===========+
0 1 2 3 7 5 6 9 4 8     # 3 <-> 7 변경됨.

0 1 2 3 4 5 6 9 7 8     # 4 <-> 7 변경됨.
0 1 2 3 4 5 6 9 7 8     # 5 <-> 5 변경됨.
0 1 2 3 4 5 6 9 7 8     # 6 <-> 6 변경됨.
0 1 2 3 4 5 6 7 9 8     # 7 <-> 9 변경됨.
0 1 2 3 4 5 6 7 8 9     # 8 <-> 9 변경됨.
```
</details>

<details><summary>python code</summary>

```py
import random

def selection_sort(data):
    # 선택된 최솟값과 swap할 대상의 인덱스
    for i in range(len(data)):
        # 아직 정렬되지 않은 데이터에 대해 최솟값 찾기 수행
        min_idx = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# before: [7, 10, 0, 8, 8, 7, 6, 0, 4, 5]
# after:  [0, 0, 4, 5, 6, 7, 7, 8, 8, 10]
```

</details><br/>

---
<!-- ################################################### -->
### 2. 삽입정렬(Insertion Sort)

> 데이터를 하나하나 확인해가며, 각 데이터를 적절한 위치에 삽입하는 방식의 정렬 알고리즘. 정렬이 필요한 원본 데이터(`data_array`)를 정렬이 된 그룹(`sorted_array`)과 정렬을 수행해야하는 그룹(`unsorted_array`)으로 나눔. 이후 `unsorted_array`에서 순차적으로 하나씩 정렬할 데이터를 `선택`하고, 선택된 데이터를 `sorted_array`의 데이터들과 대소 비교를 수행하여 적절한 위치에 삽입하는 동작을 반복함.

* 필요할 때만 위치를 바꾸는 방식
* 따라서 `거의 정렬이 되어 있는 데이터를 대상`으로 정렬을 수행할 때 효율적.
* 최선의 경우 `O(N)`의 시간복잡도


<details><summary>Sample</summary>

```
# Original

+----------------------- 정렬된 것으로 간주하고, 소팅 시작
|
V
7 5 9 0 3 1 6 2 4 8

# Sorting Setps
7 5 9 0 3 1 6 2 4 8   | 변경대상 |   변경 내용
----------------------+--------+-----------------------
5 7 9 0 3 1 6 2 4 8   |   5    |  [7 5]
                      |        |  [5 7]
5 7 9 0 3 1 6 2 4 8   |   9    |  [5 7 9] (변경되지 않음)
                      |        |  [5 7 9]
0 5 7 9 3 1 6 2 4 8   |   0    |  [5 7 9 0]
                      |        |  [0 5 7 9]
0 3 5 7 9 1 6 2 4 8   |   3    |  [0 5 7 9 3]
                      |        |  [0 3 6 7 9]
0 1 3 5 7 9 6 2 4 8   |   1    |  [0 3 5 7 9 1]
                      |        |  [0 1 3 5 7 9]
0 1 3 5 6 7 9 2 4 8   |   6    |  [0 1 3 5 7 9 6]
                      |        |  [0 1 3 5 6 7 9]
0 1 2 3 5 6 7 9 4 8   |   2    |  [0 1 3 5 6 7 9 2]
                      |        |  [0 1 2 3 5 6 7 9]
0 1 2 3 4 5 6 7 9 8   |   4    |  [0 1 2 3 5 6 7 9 4]
                      |        |  [0 1 2 3 4 5 6 7 9]
0 1 2 3 4 5 6 7 8 9   |   8    |  [0 1 2 3 4 5 6 7 9 8]
                      |        |  [0 1 2 3 4 5 6 7 8 9]
```
</details>


<details><summary>python code</summary>

```py
import random

def insertion_sort(data):
    for i in range(1, len(data)):
        # 삽입할 데이터를 한 칸씩 왼쪽으로 이동하며, 크기 비교 
        for j in range(i, 0, -1):
            # 저산보다 큰 데이터를 만나면 swap
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j -1]
            
            else: # 자신보다 작은 데이터를 만나면 해당 위치에서 정지
                break

    return data

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = insertion_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# Sample Output
# before: [0, 8, 1, 1, 4, 1, 9, 7, 9, 7]
# after:  [0, 1, 1, 1, 4, 7, 7, 8, 9, 9]
```

</details></br>

---
<!-- ################################################### -->
### 3. 퀵정렬(Quick Sort)

> 정렬 대상 내의 특정 데이터가 정렬 이후 위치할 곳을 찾는 방식으로, 리스트의 모든 요소를 대상으로 반복적으로 수행됨. 기준 데이터(`Pivot`)를 설정하고 해당 데이터보다 `작은` 데이터들은 `좌측`으로 `큰` 데이터들은 `우측`으로 모두 위치하도록 순서를 변경함. 이를 통해 정렬 이후 리스트 내에서 `기준 데이터가 위치할 인덱스가 결정됨`. 특정 Pivot을 대상으로 정렬이 완료되면, Pivot 값 좌측은 Pivot 값보다 작은 값만, 우측은 Pivot 값보다 큰 값만 위치하기 때문에, 이후 `분할 정복` 방식으로 Pivot을 선택하고 정렬하는 과정을 수행할 수 있음.

<br/>

:point_right:&nbsp; `Pivot` 이란?

* 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준이 되는 값.

* 퀵 정렬을 수행하기 전에 피벗을 어떻게 설정할지 미리 명시해야 함.

* Pivot을 설정하고, 리스트를 분할하는 방법에 따라, 다양한 방식으로 퀵 정렬을 구분할 수 있음.

* 대표적인 Pivot 설정 방법은 `리스트의 첫 번째 데이터를 Pivot으로` 정하는 `호어 분할(Hore Partition)` 방식이 있음.

* 해당 Pivot에 대해 정렬 수행이 완료되면, 해당 Pivot의 위치는 정렬 후의 위치가 됨.

  * 피벗 기준으로, 피벗의 `왼쪽에는 피벗보다 작은 데이터`가 위치하고, `오른쪽에는 피벗보다 큰 데이터들`이 위치함. 이와 같은 작업을 분할(Division) 또는 파티션(Partition)이라고 함.

<br/>

:point_right:&nbsp; `Pivot`을 설정한 이후, 설정된 `Pivot`을 기준으로 데이터 분할 방법?
  
* 리스트의 왼쪽에서부터 `Pivot`보다 큰 데이터를 찾음.

* 리스트의 오른쪽에서부터 `Pivot`보다 작은 데이터를 찾음.

* 큰 데이터와 작은 데이터의 위치를 서로 교환함.

* 왼쪽에서부터 찾는 값(`Pivot`보다 큰 값)의 인덱스가 오른쪽에서부터 찾는 값(`Pivot`보다 작은 값)의 인덱스보다 커질 때(`값이 엇갈릴 때 까지`) 까지, 이와 같은 교환 과정을 반복함.


:point_right:&nbsp; 퀵 정렬의 구현

* 퀵 정렬은 재귀함수의 형태로 구현 시, 간결하게 구현 가능함.

* `재귀 동작`: 특정한 리스트에서 피벗을 설정하여 정렬을 수행. 

* `재귀 종료 조건`:
  
  * `더 이상 정렬할 대상이 없을 때` = `정렬 대상 리스트 원소의 갯수가 1개일 때`

<br/>

<details><summary>Sample</summary>

```bash
#-------------------Original Data-----------------------#
+----------------------- Pivot (Hore Partition)
|
V
5 7 9 0 3 1 6 2 4 8
#-------------------------------------------------------#

#-------------------Sorting Steps-----------------------#
## Part I: 특정 Pivot을

### 4 <-> 7 위치 변경
+----------------------- Pivot
| +--------------------- Pivot 보다 큰 값:  7
| |             +------- Pivot 보다 작은 값: 4 
| |             |
V V             V
5 7 9 0 3 1 6 2 4 8     [위치 변경 전]
5 4 9 0 3 1 6 2 7 8     [위치 변경 후]
----[피벗보다 큰 값 탐색]--->
<--[피벗보다 작은 값 탐색]---

### 2 <-> 9 위치 변경
+----------------------- Pivot
|   +------------------- Pivot 보다 큰 값:  9
|   |         +--------- Pivot 보다 작은 값: 2 
|   |         |
V   V         V
5 4 9 0 3 1 6 2 7 8     [위치 변경 전]
5 4 2 0 3 1 6 9 7 8     [위치 변경 후]

### 5(피벗) <-> 1(작은 데이터) 위치 변경: "분할 완료"
+----------------------- Pivot
|         +------------- Pivot 보다 작은 값: 1 
|         | +----------- Pivot 보다 큰 값:  6
|         | |
V        (V V)---------- 엇갈린 상태: bigdata_idx > smalldata_idx
5 4 2 0 3 1 6 9 7 8     [위치 변경 전]
1 4 2 0 3 5 6 9 7 8     [위치 변경 후]
|       | | |     | 
+-------+ | +-----+
   (1)   (2)  (3)

피벗 기준으로, 피벗의 왼쪽에는 피벗보다 작은 데이터가 위치하고, 오른쪽에는 피벗보다 큰 데이터들이 위치함. 이와 같은 작업을 분할(Division) 또는 파티션(Partition)이라고 함.
(1): 피벗보다 작은 값
(2): 피벗
(3): 피벗보다 큰 값

#-------------------------------------------------------#
## Part II: (1)에 대해, 새로운 피벗값인 "1" 으로 정렬 수행
   (1)   (2)  (3)
+-------+ | +-----+
|       | | |     | 
1 4 2 0 3 5 6 9 7 8
|
[새로운 피벗]: 1

#-------------------------------------------------------#
## Part III: (3)에 대해, 새로운 피벗값인 "6" 으로 정렬 수행
   (1)   (2)  (3)
+-------+ | +-----+
|       | | |     | 
1 4 2 0 3 5 6 9 7 8     
            |
        [새로운 피벗]: 6

```
</details>

<details><summary>Code</summary>

```python
import random

def quicksort(data, start, end):
    if start >= end: # 원소가 1개인 경우 재귀 종료
        return
    
    pivot = start       # 첫번 째 원소의 인덱스를 피벗으로 설정

    left = pivot + 1    # 피벗보다 큰 값을 찾기 위한 인덱스의 시작 값을 
                        # 피벗의 바로 우측 값으로 설정

    right = end         # 피벗보다 작은 값을 찾기 위한 인덱스의 시작 값을
                        # 리스트의 가장 우측 인덱스로 설정

    # left와 right이 엇갈릴 때까지, 피벗을 기준으로 좌측과 우측 데이터의 위치 교환을 반복
    while left <= right:
        # 피벗보다 큰 데이터의 인덱스 찾기
        while left <= end and data[left] <= data[pivot]:
            left += 1
        
        # 피벗보다 작은 데이터의 인덱스 찾기
        while start < right and data[right] >= data[pivot]:
            right -= 1

        # left와 right이 엇갈린 경우
        if left >= right:
            # 작은 데이터와 피벗의 위치를 swap
            data[pivot], data[right] = data[right], data[pivot]

        # left와 right이 엇갈리지 않은 경우
        else:
            # 작은 데이터와 큰 데이터의 위치를 swap
            data[right], data[left] = data[left], data[right]

    # 분할 완료
    quicksort(data, start, right - 1)    # 피벗의 좌측 데이터들을 대상으로 정렬 수행
    quicksort(data, left, end)      # 피벗의 우측 데이터들을 대상으로 정렬 수행



data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(data))
quicksort(data, 0, len(data) - 1)
print('after:  {}'.format(data))

# before: [7, 3, 0, 5, 8, 6, 1, 10, 7, 8]
# after:  [0, 1, 3, 5, 6, 7, 7, 8, 8, 10]
```
</details><br/>

---
<!-- ################################################### -->
### 4. 계수정렬(Counting Sort)

> 데이터의 크기 범위가 제한되어, 정수 형태로 표현이 가능할 때만 사용 가능한 매우 빠른 정렬 알고리즘. 데이터의 갯수가 `N`개 이고, 데이터 중 최대값이 `K`일 때, 최악의 경우에도 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20%2B%5C%20K)" />의 수행 시간을 보장함. 데이터의 정렬 정보를 저장하는 배열에, 데이터 값을 인덱스로하여 값을 저장하는 방식을 사용. 

* 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차가 `1,000,000(백만)`을 넘지 않을 때 효과적으로 사용 가능.

* 계수 정렬과 (약간 느리지만)유사한 성능을 갖지만, 계수 정렬 보다 처리할 수 있는 정수의 범위가 더 큰 정렬 알고리즘으로는 `기수(Radix) 정렬`이 있음.
  
  * 하지만 코딩테스트에서 `기수 정렬`의 출제 빈도는 매우 낮은 편.

<details><summary>code</summary>

```python
import random

def counting_sort(data):
    sorted_data = []
    count = [0] * (max(data) + 1)

    for i in range(len(data)):
        count[data[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            # print(i, end=' ')
            sorted_data.append(i)

    return sorted_data

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = counting_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# before: [7, 3, 5, 7, 5, 6, 3, 10, 4, 8]
# after:  [3, 3, 4, 5, 5, 6, 7, 7, 8, 10]
```

</details>


<br/><br/>

---
<!-- ################################################### -->
[[뒤로](../../cheatsheet/sort.md)] / [[위로](#sort)]

## :two:&nbsp; 소팅 알고리즘의 시간복잡도/공간복잡도 비교

> `n`: 데이터의 갯수, `r` 정렬될 수의 범위.

<table>
    <thead>
        <tr>
            <th>Algorithms</th>
            <th colspan="3" align="center">Time Complixity</th>
            <th colspan="3" align="center"><img src="https://chart.apis.google.com/chart?cht=tx&chl=times(n)_%7Bsec%7D" /></th>
            <th colspan="2" align="center">Space Complexity</th>
        </tr>
        <tr>
            <th>&nbsp;</th>
            <th>Worst<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=O" /> </th>
            <th>Best<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega" /></th>
            <th>Average<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta" /></th>
            <th>N=100</th>
            <th>N=1,000</th>
            <th>N=10,000</th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=mem_%7Bworst%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=mem_%7Bavg%7D" /></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>선택 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /></td>
            <td>0.0123</td>
            <td>0.354</td>
            <td>15.475</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>삽입 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n^2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>퀵 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>0.00156</td>
            <td>0.00343</td>
            <td>0.0312</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(%5Clog_%7B%7DN)" /></td>
        </tr>
        <tr>
            <td>내장 정렬 라이브러리</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7Dn)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7Dn)" /></td>
            <td>0.00000753</td>
            <td>0.0000365</td>
            <td>0.000248</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>계수 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%2Br)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%2Br)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%2Br)" /></td>
        </tr>
        <tr>
            <td>버블 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N^2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(N%5E2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>병합 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
        </tr>
    </tbody>
</table>

* 각 소팅 알고리즘의 시간 측정 환경: Intel(R) Core(TM)i7-7500U CPU @ 2.70GHz. 2 Core 환경

* [더 많은 정렬 알고리즘과 각 알고리즘의 분류](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

* 파이썬의 built-in sort 함수는 [Timsort 알고리즘](https://en.wikipedia.org/wiki/Timsort)을 사용함.

  * 내부적으로 C 기반으로 구현되었고, 최적화 테크닉이 들어가 훨씬 빠르게 동작함.

### 1. 선택정렬

:point_right:&nbsp; Worst-Case Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /> 번 swap 수행.

:point_right:&nbsp; Best-Case  Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(1)" /> 번 swap 수행.

:point_right:&nbsp; Average    Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n)" /> 번 swap 수행.

<br/>

### 2. 삽입정렬

:point_right:&nbsp; Worst-Case Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 swap 수행.

:point_right:&nbsp; Best-Case  Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(1)" /> 번 swap 수행.

:point_right:&nbsp; Average    Performance

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 swap 수행.


<br/>

### 3. 퀵정렬

:point_right:&nbsp; Worst-Case Performance: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" />

:point_right:&nbsp; Best-Case  Performance

* Simple Partition: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%7Bn%7D)" />

* Three-way Partition and equal keys: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" />

:point_right:&nbsp; Average    Performance: <img src="https://chart.apis.google.com/chart?cht=tx&chl=n%5Clog%7B%7D%7Bn%7D" />

<br/>

### 4. 계수정렬

> 모든 데이터가 양의정수이고, 데이터 갯수가 `N`, 데이터 중 최대값의 크기가 `K`인 상태.

:point_right:&nbsp; 시간 복잡도: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20%2B%5C%20K)" />
  
* 정렬 정보를 저장하는 배열에 데이터를 삽입하는 동작: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" />
  
* 정렬 정보를 저장하는 배열을 순차적으로 방문하는 동작: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(K)" />


:point_right:&nbsp; 공간 복잡도: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20%2B%5C%20K)" />

<table>
<thead>
<tr>
<th>배열 크기</th>
<th>할당 메모리(MB)</th>
<th>할당 시간(sec)</th>
</tr>
</thead>
<tbody>
<tr>
<td>100,000(십만)</td>
<td>0.7MB</td>
<td>0.00007 sec</td>
</tr>
<tr>
<td>1,000,000(백만)</td>
<td>7MB</td>
<td>0.00128 sec</td>
</tr>
<tr>
<td>10,000,000(천만)</td>
<td>76MB</td>
<td>0.01291 sec</td>
</tr>
<tr>
<td>100,000,000(억)</td>
<td>762MB</td>
<td>0.60375 sec</td>
</tr>
</tbody>
</table>

```python
sys.getsizeof([0]*100000) // (2 ** 20)      # 십만, 0.7 MB, 0.00007 sec
sys.getsizeof([0]*1000000) // (2 ** 20)     # 백만,   7 MB, 0.00128 sec
sys.getsizeof([0]*10000000) // (2 ** 20)    # 천만,  76 MB, 0.01291 sec
sys.getsizeof([0]*100000000) // (2 ** 20)   # 일억, 762 MB, 0.60375 sec

[0 for _ in range(size)] # List Comprehension으로 생성할 경우 현저히 느려짐.
```

<br/>

---
## 읽어볼만한 문서

* [What are Sorting Algorithms?](https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/): 각 정렬 알고리즘에 대한 시간/공간 복잡도 정리가 잘 되어있음.