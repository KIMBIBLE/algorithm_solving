# Sort

## 소팅 알고리즘의 종류

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

<!-- ################################################### -->
### 2. 삽입정렬

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

<!-- ################################################### -->

### 3. 퀵정렬


### 4. 계수정렬


---
## 소팅 알고리즘의 시간복잡도/공간복잡도 비교

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

### 1. 선택정렬

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5BC_%7Bmin%7D%5C%20%3D%5C%20C_%7Bave%7D%5C%20%3D%5C%20C_%7Bmax%7D%5C%20%3D%5C%20%5C%20%5Csum_%7Bi%3D1%7D%5E%7BN-1%7D%5C%20N%5C%20-%5C%20i%5C%20%5C%20%3D%5C%20%5Cfrac%7BN(N%5C%20-%5C%201)%7D%7B2%7D%5C%20%3D%5C%20O(N%5E2)%5C%5D" />



<br/><br/>

---
## 읽어볼만한 문서

* [What are Sorting Algorithms?](https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/): 각 정렬 알고리즘에 대한 시간/공간 복잡도 정리가 잘 되어있음.