# Algorithm Overview

해당 문서에서는 문제를 해결하는 방법인 `알고리즘`과, 알고리즘 클래스 설계의 기초가 되는 일반적인 방법 또는 접근 방식인 `알고리즘 패러다임`에 대해 토픽별로 다루고있습니다.

<br/>

---
## :open_file_folder:&nbsp; 구현

|Documentation|Description|
|-|-|
|[구현 문제 유형](./algorithms/implementation/impl_cases.md)|구현 문제 유형|

<br/>

---
## :open_file_folder:&nbsp; 정렬 알고리즘

|Documentation|Description|
|-|-|
|[정렬 알고리즘의 종류 I - 코딩테스트용](./cheatsheet/../algorithms/sorting/sorting_algorithms.md)|선택정렬, 삽입정렬, 퀵정렬, 계수정렬 설명|
|소팅 알고리즘의 종류 II|병합정렬, 버블정렬, 힙정렬, 쉘소트, ... 설명|
|[정렬 알고리즘의 시간복잡도/공간복잡도 비교](./cheatsheet/../algorithms/sorting/sorting_time_complexity.md)|정렬 알고리즘의 시간복잡도 분석|
|[프로그래밍 언어별 정렬 알고리즘의 활용](./cheatsheet/../algorithms/sorting/sorting_in_various_programming_languages.md.md)|프로그래밍 언어별 정렬 알고리즘의 활용 방법 정리|
|[정렬 알고리즘의 문제 유형](./cheatsheet/../algorithms/sorting/sorting_cases.md)|정렬 알고리즘의 종류, 구현, 시간/공간 복잡도 정리 및 분석|

<br/>

---

## :open_file_folder:&nbsp; 탐색 알고리즘

|Documentation|Description|
|-|-|
|선형 탐색(Linear Search)|순차적 탐색|
|Jump/Block Search|정렬된 배열에서의 탐색을 통해 탐색의 효율성을 높이는 방법|
|이진 탐색(Binary Search)|정렬된 배열에서의 탐색을 통해 탐색의 효율성을 높이는 방법|
|[이진 탐색(Binary Search): 배열](./../dongbin_book/chap7_binary_search/README.md)|array를 활용한 이진탐색 구현|
|[완전 탐색](./algorithms/exhaustive_search/README.md)|가능한 모든 경우의 수를 전부 체크하여 정답을 찾는 방법|
|Interpolation Search|균일하게 분포된 정렬된 배열에서의 탐색|

</br>

---

## :open_file_folder:&nbsp; Graphs

|Documentation|Description|
|-|-|
|[DFS 알고리즘](./algorithms/dfs.md)|깊이 우선 탐색|
|[BFS 알고리즘](./algorithms/bfs.md)|너비 우선 탐색|
|DFS & BFS 문제 유형|DFS & BFS 문제 유형|
|크루스칼 알고리즘(Kruskal’s Algorithm)|가중 무방향 그래프에 대한 최소 스패닝 트리(MST) 찾기|
|다익스트라 알고리즘(Dijkstra Algorithm)|단일 정점에서 모든 그래프 정점에 대한 최단 경로 찾기|
|벨만-포드 알고리즘(Bellman-Ford Algorithm)|단일 정점에서 모든 그래프 정점에 대한 최단 경로 찾기|
|플로이드-워셜 알고리즘(Floyd-Warshall Algorithm)|모든 정점 쌍 사이의 최단 경로 찾기|
|싸이클 찾기(Detect Cycle)|directed/undirected 그래프의 싸이클 찾기(DFS 및 Disjoint Set 기반 버전)|
|프라임 알고리즘(Prim’s Algorithm)|가중 무방향 그래프에 대한 최소 스패닝 트리(MST) 찾기|
|Topological Sorting|DFS 구현|
|Articulation Points|Tarjan's algorithm (DFS based)|
|Bridges|DFS based algorithm|
|Eulerian Path and Eulerian Circuit|Fleury's algorithm - Visit every edge exactly once|
|Hamiltonian Cycle|Visit every vertex exactly once|
|Strongly Connected Components|Kosaraju's algorithm|
|Travelling Salesman Problem|shortest possible route that visits each city and returns to the origin city|

</br>


---

## :open_file_folder:&nbsp; Cryptography

|Documentation|Description|
|-|-|
|Polynomial Hash|rolling hash function based on polynomial|
|Rail Fence Cipher|a transposition cipher algorithm for encoding messages|
|Caesar Cipher|simple substitution cipher|
|Hill Cipher|substitution cipher based on linear algebra|

</br>

---

## :open_file_folder:&nbsp; Greedy Paradigm

|Documentation|Description|
|-|-|
|[Greedy 알고리즘](./algorithms/greedy/README.md)|미래를 고려하지 않고 현재의 최선의 선택을 반복하는 솔루션|
|Greedy 문제 유형|Greedy 패러다임을 적용하여 해결 가능한 PS 문제 유형|

</br>

---
## :open_file_folder:&nbsp; Dynamic Programming Paradigm


|Documentation|Description|
|-|-|
|[다이나믹 프로그래밍 기본](./algorithms/dynamic_programming/README.md)|다이나믹 프로그래밍 설명과 DP 문제의 접근 방법 설명|
|[다이나믹 프로그래밍 문제 유형](./algorithms/dynamic_programming/dp_case.md)|DP 문제 유형|

</br>

---

## :open_file_folder:&nbsp; Brute Force Paradigm

|Documentation|Description|
|-|-|
|Brute Force|Brute Force 패러다임 설명|
|Brute Force 문제 유형|Brute Force 패러다임으로 해결 가능한 PS 문제 유형|


</br>

---

## :open_file_folder:&nbsp; Divide and Conquer Paradigm

|Documentation|Description|
|-|-|
|Divide & Conquer|Divide & Conquer 패러다임 설명|
|Divide & Conquer 문제 유형|Divide & Conquer 패러다임으로 해결 가능한 PS 문제 유형|


</br>

---

## :open_file_folder:&nbsp; Backtracking Paradigm

|Documentation|Description|
|-|-|
|Backtracking|Backtracking 패러다임 설명|
|Backtracking 문제 유형|Backtracking 패러다임으로 해결 가능한 PS 문제 유형|


</br>

---

## :open_file_folder:&nbsp; Branch & Bound Paradigm

|Documentation|Description|
|-|-|
|Branch & Bound|Branch & Bound 패러다임 설명|
|Branch & Bound 문제 유형|Branch & Bound 패러다임으로 해결 가능한 PS 문제 유형|


<br/>

---
## :open_file_folder:&ensp; 기타 알고리즘

* [파라메트릭 서치](./algorithms/parametric_search.md)

<br/>

---

## 참고

* https://github.com/trekhleb/javascript-algorithms