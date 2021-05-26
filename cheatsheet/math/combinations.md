# Combinations: $nCr =$$n \choose r$$= \frac{n!\times r!}{(n-r)!}$

<img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5C%20%7Bn%5C%20%5Cchoose%5C%20r%7D%5C%20%3D%5C%20%5Cfrac%7Bn!%5C%20%5Ctimes%5C%20r!%7D%7B(n%5C%20-%5C%20r)!%7D" /><br/>

> 순서가 없는 순열로, 전체에서 특정 개수를 선택하는 경우

1. 공식

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=nCr%5C%20%3D%5C%20%5Cfrac%7Bn!%5Ctimes%5C%20r!%7D%7B(n-r)!%7D" />

2. Python `itertools` 모듈의 `combinations` 함수

    ```py
    from itertools import combinations

    nums = [1, 2, 3, 4]
    choose = list(combinations(nums, 2))
    print(choose)
    ```

3. 시간복잡도

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(%5C%20%7Bn%5C%20%5Cchoose%5C%20k%7D%5C%20)%5C%20%3D%5C%20O(%5C%20min(%5C%20n%5Ek%2C%5C%20n%5E%7Bn%5C%20-%5C%20k%7D%5C%20)%5C%20)" />