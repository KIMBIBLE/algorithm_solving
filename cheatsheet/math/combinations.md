# Combinations: $nCr =$$n \choose r$$= \frac{n!\times r!}{(n-r)!}$

> 순서가 없는 순열로, 전체에서 특정 개수를 선택하는 경우

1. 공식

    $nCr = \frac{n!\times r!}{(n-r)!}$

2. Python `itertools` 모듈의 `combinations` 함수

    ```py
    from itertools import combinations

    nums = [1, 2, 3, 4]
    choose = list(combinations(nums, 2))
    print(choose)
    ```

3. 시간복잡도

    $O(nCk)=O(min(n^k, n^{n-k}))$