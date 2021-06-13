# Combinations

<img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5C%20%7Bn%5C%20%5Cchoose%5C%20r%7D%5C%20%3D%5C%20%5Cfrac%7Bn!%5C%5C%20%7D%7B(n%5C%20-%5C%20r)!r!%7D" /><br/>

> 순서가 없는 순열로, 전체에서 특정 개수를 선택하는 경우

## 1. 공식

<img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5Cfrac%7Bn!%5C%20%7D%7B(n-r)!r!%7D" />



## 2. 이항계수의 성질

### 1) 성질 1
<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7Bn%5C%20%5Cchoose%5C%20r%7D%5C%20%3D%5C%20%7Bn%5C%20%5Cchoose%5C%20n%5C%20-%5C%20k%7D" />

<br/>

### 2) 성질 2

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20%3D%5C%20%7Bn%5C%20-%5C%201%5C%20%5Cchoose%5C%20k%7D%5C%20%2B%5C%20%7Bn%5C%20-%5C%201%5C%20%5Cchoose%5C%20k%5C%20-%5C%201%7D" />

<br/>

### 3) 성질 3

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5B%5C%20%5Csum_%7Bk%3D1%7D%5E%7B%5Cinfty%7D%5C%20%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20%3D%5C%202%5En%5C%20%5C%5D" />

## 3. Python `itertools` 모듈의 `combinations` 함수

    ```py
    from itertools import combinations

    nums = [1, 2, 3, 4]
    choose = list(combinations(nums, 2))
    print(choose)
    ```

## 4. 시간복잡도

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(%5C%20%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20)%5C%20%3D%5C%20O(%5C%20min(%5C%20n%5Ek%2C%5C%20n%5E%7Bn%5C%20-%5C%20k%7D%5C%20)%5C%20)" />