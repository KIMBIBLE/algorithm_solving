# Prob 01 writeup

## 제한

시간: 1초, 메모리: 128 MB

<br/>

## 문제 분석

중복되지 않는 정수 값을 가지는 `N` 개의 데이터 집합에서,
`M` 개의 입력값으로 주어진 정수 값의 존재 여부를 식별하는 문제.

```
1 <= N, M <= 1,000,000
1 <= 데이터의 범위 <= 1,000,000
```

`N` 개의 데이터에서 해당 정수가 존재하는지를 `M` 번만큼 확인해야 하니까
선형 탐색을 활용하면 시간복잡도는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20*%5C%20M)" />이 나옴.

하지만 `실행 시간 1초를 기준`으로, <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5E2)" /> 알고리즘은 `권장되는 입력의 크기`가 `1만` 정도. 따라서 다른 탐색 방법을 활용해야 함.

`M` 번 확인하는 것은 줄일 수 없으니 `N`을 줄이기 위해 이진 탐색 방법 활용하면,
<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(M%5C%20log%5C%20N)" />으로 탐색이 가능함.

이 때, 이진탐색을 사용하려면 `N`개의 데이터들이 정렬되어잇어야 하기 때문에, 정렬 과정이 필요함.

따라서 `N개의 데이터 정렬`과 `이진 탐색`의 시간 복잡도는 최종적으로 <img src="https://chart.apis.google.com/chart?cht=tx&chl=(N%5C%20%2B%5C%20M)%5C%20%5Clog%7B%7D%7BN%7D" />이 됨.

<br/>

## 입출력 예시

### 입력 예시

```
5
8 3 7 9 2
3
5 7 9
```

### 출력 예시

```
no yes yes
```