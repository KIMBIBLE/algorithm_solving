# Combinations

<img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5C%20%7Bn%5C%20%5Cchoose%5C%20r%7D%5C%20%3D%5C%20%5Cfrac%7Bn!%5C%5C%20%7D%7B(n%5C%20-%5C%20r)!r!%7D" /><br/>

> 순서가 없는 순열로, 전체에서 특정 개수를 선택하는 경우

## 1. 공식

<img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5Cfrac%7Bn!%5C%20%7D%7B(n-r)!r!%7D" />

* n개 중 r개 선택
  
  * n개의 집합에서 하나씩 원소 r개까지 뽑음
  
  * 선택된 순서에 해당되는 r!개의 경우는 제외함.

## 2. 이항계수의 성질

### 1) 성질 1
<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20%3D%5C%20%7Bn%5C%20%5Cchoose%5C%20n%5C%20-%5C%20k%7D" />

* n개의 집합에서 k개의 원소를 선택하는 것은 n개의 집합에서 n-k개의 원소를 선택하지 않는 것과 동일한 의미.

<br/>

### 2) 성질 2

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20%3D%5C%20%7Bn%5C%20-%5C%201%5C%20%5Cchoose%5C%20k%7D%5C%20%2B%5C%20%7Bn%5C%20-%5C%201%5C%20%5Cchoose%5C%20k%5C%20-%5C%201%7D" />

* n개의 집합에서 k개의 원소가 선택 된 state는 다음과 같은 의미.
  
  * n개의 집합을 n-1개와 1개로 나누면, 다음 두가지 경우로 분류 가능.
    
    * n-1개의 집합에서 k개를 선택하는 경우(나머지 원소 1개짜리 집합에서는 선택하지 않음).
    
    * n-1개의 집합에서 k-1개만큼 뽑고, 나머지 1개짜리 집합에서 선택을 하는 경우.

<br/>

### 3) 성질 3

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5B%5C%20%5Csum_%7Bk%3D0%7D%5E%7Bn%7D%5C%20%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20%3D%5C%202%5En%5C%20%5C%5D" />

* n개의 집합에서 {0개, 1개, 2개, ...., n개}의 원소를 선택하는 경우를 모두 합치면, 

* n개의 집합을 대상으로 할 수 잇는 모든 선택(뽑거나 안뽑거나)과 같은 의미

<br/>

## 3. Python `itertools` 모듈의 `combinations` 함수

    ```py
    from itertools import combinations

    nums = [1, 2, 3, 4]
    choose = list(combinations(nums, 2))
    print(choose)
    ```

## 4. 시간복잡도

<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(%5C%20%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20)%5C%20%3D%5C%20O(%5C%20min(%5C%20n%5Ek%2C%5C%20n%5E%7Bn%5C%20-%5C%20k%7D%5C%20)%5C%20)" />