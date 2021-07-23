# Prob 02 writeup

## 제한

시간: 2초, 메모리: 128MB

<br/>

## 문제 분석

떡의 갯수: 1 <= N <= 1,000,000 (백만)

요청한 떡의 길이: 1 <= M <= 2,000,000,000 (20억)

N개의 떡의 높이들: <img src="https://chart.apis.google.com/chart?cht=tx&chl=x_1" />, <img src="https://chart.apis.google.com/chart?cht=tx&chl=x_2" />, ..., <img src="https://chart.apis.google.com/chart?cht=tx&chl=x_N" /> (각 떡의 높이는 10억 미만의 양의 정수)

> `N개의 떡들` 각각에 대해, `자르고자 하는 떡의 높이(H)` 만큼 `뺀 나머지의 합`이, `최소 M` 만큼 될 수 있도록 하는 `최대값 H`를 구하기.

<br/>

### :bulb: H를 어떻게 정해야할까?

1. 브포로 `H`값들을 순차 탐색?

    떡의 높이의 최댓값이 10억이기 떄문에, <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(H)" />의 시간 복잡도를 갖는 순차 탐색 방법은 사용 불가능함.

    따라서, <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(%5Clog%7B%7D%7BH%7D)" /> 탐색 알고리즘을 사용해야 함.

2. 이진 탐색

    `start = 0, end = 1,000,000,000`으로 이진 탐색을 수행하며 `적절한 H 값`을 결정. 최적값을 찾아야 하기 때문에 만족하는 조건이 발견되자마자 탐색을 종료하는 것이 아닌, 이진 탐색 수행 중에 조건을 만족하는 값을 저장하고, 탐색 종료 후 이를 기반으로 최적해를 결정하면 됨.
    
    ```py
    total = 0
    for x in array:
        if x > H:
            total += x - H
    ```

    * Case 1: `total < M`

        떡을 더 잘라봐야하므로 현재 `H`값을 기록하고, `start = H, end = end`로 다시 탐색.

    * Case 2: `total >= M`

        떡을 덜 잘라야하므로, `start = start, end = H`로 다시 탐색.


    :bulb:&ensp; 시간복잡도?

    이진 탐색의 범위(`R`)가 `10억 미만`이고, end 값을 찾는 과정에서 선형 탐색을 한번 진행했으니 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)%5C%20%2B%5C%20O(%5Clog%7B%7D%7BR%7D)" />의 시간 복잡도가 나옴.

    최악의 케이스 연산 시간 계산
    
    * 이진 탐색의 범위가 `10억 - 1`이기 떄문에, <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5Clog%7B%7D%7B1%2C000%2C000%2C000%7D%5C%20%5Capprox%5C%2020" />회의 연산이 필요
    
    * 범위의 최댓값 도출을 위한 선형 탐색 시 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)%5C%20%3D%5C%20O(1,000,000)" />이 나옴. <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" />복잡도의 알고리즘은 N값이 1억정도가 될 때 1초가 소요되기 떄문에, 제한 시간 2초 안에 넉넉하게 수행 가능.

<br/>

## 입출력 예시

### 입력 예시

```txt
4 6
19 15 10 17
```

### 출력 예시

```txt
15
```