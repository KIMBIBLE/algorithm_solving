# Data Structrue

## :one:&ensp; 배열

### 1. Python

* [1차원 배열의 주요 메서드와 특징: List](./array/python/one_dimensional_array.md)

* [다차원(2차원 이상) 배열의 생성 및 사용: List](./array/python/multi_dimensional_array.md)

* [[외부 링크] Python, Memory, and Objects](https://towardsdatascience.com/python-memory-and-objects-e7bec4a2845): mutable object, immutable object, interning 개념 설명 잘되어있음.

* [[외부 링크] assignment("=") vs shallow copy vs deep copy](https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86)

* [배열 내 데이터의 탐색: 순차탐색](./array/python/sequential_search.md)

* [배열 내 데이터의 탐색: 이진탐색](./../../dongbin_book/chap7_binary_search/README.md)

<br/>

---
## :two:&ensp; 스택

### 0. Overview

원소 삽입 삭제의 시간복잡도가 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />로 매우 빠름. 하지만 이론상 스택의 top을 제외한 나머지 스택 내 데이터의 탐색 시 원소를 하나씩 꺼내어 옮겨 담으면서 수행해야하는 단점이 있음.


:bulb:&ensp; 언제 사용할까?

> 재귀 알고리즘이나 백트래킹이 필요한 작업에서 활용하기 좋음.

<br/>

:bulb:&ensp; 대표적인 스택 문제

* 괄호 검사

* 역순 문자열 만들기

* 후위 표기법으로의 변환

<br/>

### 1. 구현

#### :pushpin:&ensp; Python 구현

* [List를 활용한 구현](./stack/python/stack_list.md)

* [deque 모듈 사용](./stack/python/stack_deque.md)


<br/>

---
## :two:&ensp; 큐

### 1. Python
* [List를 활용한 구현](./queue/python/queue_list.md)

* [deque 모듈 사용](./queue/python/queue_deque.md)

<br/>

---
## :three:&ensp; 그래프

### 1. Python 

* [인접행렬 구현](./graph/python/adjacent_matrix.md)

* [인접 리스트 구현](./graph/python/adjacent_list.md)

* [간선리스트 구현](./graph/python/edge_list.md)

* Edge Cases

<br/>

---
## :four:&ensp; 트리
### 1. Python 


<br/>

---

## :five:&ensp; 해시 테이블
### 1. Python 


<br/>

---




