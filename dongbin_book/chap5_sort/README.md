# Sort

## 소팅 알고리즘의 종류

### 1. 선택정렬

> 최소값 찾기(선택)를 반복하는 알고리즘. 무작위 데이터 리스트에서 가장 작은 값을 선택하여 리스트의 맨 앞의 요소와 교환함. 이후 선택이 완료된 데이터 리스트의 맨 앞 요소를 제외한 나머지 데이터들에 대해 최소값 찾기를 반복함.

<details><summary>python code</summary>

```py
import random

def selection_sort(data_to_sort):
    for i in range(len(data_to_sort) - 1):
        min_idx = i
        for j in range(i + 1, len(data_to_sort)):
            if data_to_sort[min_idx] > data_to_sort[j]:
                min_idx = j
        data_to_sort[i], data_to_sort[min_idx] = data_to_sort[min_idx], data_to_sort[i]

    return data_to_sort

unsorted_data = [random.randint(0, 10) for _ in range(10)]
print('before: {}'.format(unsorted_data))
sorted_data = selection_sort(unsorted_data)
print('after:  {}'.format(sorted_data))

# Sample Output
# before: [3, 2, 4, 0, 5, 2, 1, 7, 1, 7]
# after:  [0, 1, 1, 2, 2, 3, 4, 5, 7, 7]
```

</details></br>


### 2. 삽입정렬


### 3. 퀵정렬


### 4. 계수정렬


---
## 소팅 알고리즘의 시간복잡도 비교

각 정렬에 소요되는 비교 횟수를 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C" />라고 했을 때, 비교 횟수의 평균은 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" />, 최대는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" />, 최소는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" />으로 표기함. 


<table>
    <thead>
        <tr>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=Algorithms" /></th>
            <th></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(C)" /></th>
            <th></th>
            <th></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=Times(N)_%7Bsec%7D" /></th>
            <th></th>
        </tr>
        <tr>
            <th></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" /></th>
            <th>N=100</th>
            <th>N=1,000</th>
            <th>N=10,000</th>
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
        </tr>
        <tr>
            <td>삽입 정렬</td>
            <td></td>
            <td></td>
            <td></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>퀵 정렬</td>
            <td></td>
            <td></td>
            <td></td>
            <td>0.00156</td>
            <td>0.00343</td>
            <td>0.0312</td>
        </tr>
        <tr>
            <td>내장 정렬 라이브러리</td>
            <td></td>
            <td></td>
            <td></td>
            <td>0.00000753</td>
            <td>0.0000365</td>
            <td>0.000248</td>
        </tr>
        <tr>
            <td>계수 정렬</td>
            <td></td>
            <td></td>
            <td></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>버블 정렬</td>
            <td></td>
            <td></td>
            <td></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>병합 정렬</td>
            <td></td>
            <td></td>
            <td></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
    </tbody>
</table><br/>


* 각 소팅 알고리즘의 시간 측정 환경: Intel(R) Core(TM)i7-7500U CPU @ 2.70GHz. 2 Core 환경
* [더 많은 정렬 알고리즘과 각 알고리즘의 분류](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

### 1. 선택정렬

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5BC_%7Bmin%7D%5C%20%3D%5C%20C_%7Bave%7D%5C%20%3D%5C%20C_%7Bmax%7D%5C%20%3D%5C%20%5C%20%5Csum_%7Bi%3D1%7D%5E%7BN-1%7D%5C%20N%5C%20-%5C%20i%5C%20%5C%20%3D%5C%20%5Cfrac%7BN(N%5C%20-%5C%201)%7D%7B2%7D%5C%20%3D%5C%20O(N%5E1)%5C%5D" />
