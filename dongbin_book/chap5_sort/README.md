# Sort

## 소팅 알고리즘의 종류

### 1. 선택정렬

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

```
</details><br/>

### 2. 삽입정렬

> 데이터를 하나하나 확인해가며, 각 데이터를 적절한 위치에 삽입하는 방식의 정렬 알고리즘. 정렬이 필요한 원본 데이터(`data_array`)를 정렬이 된 그룹(`sorted_array`)과 정렬을 수행해야하는 그룹(`unsorted_array`)으로 나눔. 이후 `unsorted_array`에서 순차적으로 하나씩 정렬할 데이터를 `선택`하고, 선택된 데이터를 `sorted_array`의 데이터들과 대소 비교를 수행하여 적절한 위치에 삽입하는 동작을 반복함.

<details><summary>python code</summary>

```py
import random

def selection_sort(data_to_sort):
    for i in range(1, len(data_to_sort)):
        for j in range(i, 0, -1):
            if data_to_sort[j - 1] > data_to_sort[j]:
                data_to_sort[j - 1], data_to_sort[j] = data_to_sort[j], data_to_sort[j -1]
            
            else:
                break

    return data_to_sort

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# Sample Output
# before: [0, 8, 1, 1, 4, 1, 9, 7, 9, 7]
# after:  [0, 1, 1, 1, 4, 7, 7, 8, 9, 9]
```

</details></br>

### 3. 퀵정렬


### 4. 계수정렬


---
## 소팅 알고리즘의 시간복잡도/공간복잡도 비교

각 정렬에 소요되는 비교 횟수를 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C" />라고 했을 때, 비교 횟수의 평균은 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" />, 최대는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" />, 최소는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" />으로 표기함. 

N: 데이터의 갯수, r 정렬될 수의 범위.

<table>
    <thead>
        <tr>
            <th>Algorithms</th>
            <th colspan="3" align="center"><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(C)" /></th>
            <th colspan="3" align="center"><img src="https://chart.apis.google.com/chart?cht=tx&chl=Times(N)_%7Bsec%7D" /></th>
            <th colspan="2" align="center">Space Complexity</th>
        </tr>
        <tr>
            <th>&nbsp;</th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" /></th>
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
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td>0.0123</td>
            <td>0.354</td>
            <td>15.475</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=1" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>삽입 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=1" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>퀵 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>0.00156</td>
            <td>0.00343</td>
            <td>0.0312</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=N" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5Clog_%7B%7DN" /></td>
        </tr>
        <tr>
            <td>내장 정렬 라이브러리</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7Dn)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7Dn)" /></td>
            <td>0.00000753</td>
            <td>0.0000365</td>
            <td>0.000248</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=N" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>계수 정렬</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%2Br)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%2Br)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=N%2Br" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=N%2Br" /></td>
        </tr>
        <tr>
            <td>버블 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N^2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N^2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=1" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>병합 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=N" /></td>
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
</table><br/>


* 각 소팅 알고리즘의 시간 측정 환경: Intel(R) Core(TM)i7-7500U CPU @ 2.70GHz. 2 Core 환경
* [더 많은 정렬 알고리즘과 각 알고리즘의 분류](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
* 파이썬의 built-in sort 함수는 [Timsort 알고리즘](https://en.wikipedia.org/wiki/Timsort)을 사용함.

### 1. 선택정렬

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5BC_%7Bmin%7D%5C%20%3D%5C%20C_%7Bave%7D%5C%20%3D%5C%20C_%7Bmax%7D%5C%20%3D%5C%20%5C%20%5Csum_%7Bi%3D1%7D%5E%7BN-1%7D%5C%20N%5C%20-%5C%20i%5C%20%5C%20%3D%5C%20%5Cfrac%7BN(N%5C%20-%5C%201)%7D%7B2%7D%5C%20%3D%5C%20O(N%5E2)%5C%5D" />
