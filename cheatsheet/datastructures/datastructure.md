# Data Structrue

## Table of Contents

1. <a href="#ds-1">Array</a>

2. <a href="#ds-2">Linked List</a>

3. <a href="#ds-3">Stack</a>

4. <a href="#ds-4">Queue</a>

5. <a href="#ds-5">Tree</a>

6. <a href="#ds-6">Heap</a>

7. <a href="#ds-7">Hash Table</a>

8. <a href="#ds-8">Graph</a>

9. <a href="#ds-9">Set</a>

<br/>

---
<h2 id="ds-1">1️⃣  Array</h2>

### 1. 구현

:pushpin:&ensp; Python 구현 

* [1차원 배열의 주요 메서드와 특징: List](./array/python/one_dimensional_array.md)

* [다차원(2차원 이상) 배열의 생성 및 사용: List](./array/python/multi_dimensional_array.md)

* [[외부 링크] Python, Memory, and Objects](https://towardsdatascience.com/python-memory-and-objects-e7bec4a2845): mutable object, immutable object, interning 개념 설명 잘되어있음.

* [[외부 링크] assignment("=") vs shallow copy vs deep copy](https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86)

* [배열 내 데이터의 탐색: 순차탐색](./array/python/sequential_search.md)

* [배열 내 데이터의 탐색: 이진탐색](./../../dongbin_book/chap7_binary_search/README.md)

* [Python Built-in List 자료형의 Operation 별 시간복잡도 정리](./array/timecomplexity.md)

<br/>

---
<h2 id="ds-2">2️⃣  Linked List</h2>

<br/>

---
<h2 id="ds-3">3️⃣  Stack</h2>

### 0. Overview

> Last in First Out(LIFO) 구조의 자료형. 원소 삽입 삭제의 시간복잡도가 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />으로 매우 빠름. 하지만 이론상 스택의 top을 제외한 나머지 스택 내 데이터의 탐색 시 원소를 하나씩 꺼내어 옮겨 담으면서 수행해야하는 단점이 있음.

<br/>

:bulb:&ensp; 언제 사용할까?

> 재귀 알고리즘이나 백트래킹이 필요한 작업에서 활용하기 좋음.

<br/>

:bulb:&ensp; 스택 자료형을 사용하는 대표적인 문제

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
<h2 id="ds-4">4️⃣  Queue</h2>

### 0. Overview

> First in First Out(FIFO) 구조의 자료형. 원소 삽입 삭제의 시간복잡도가 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />으로 매우 빠름.

<br/>

:bulb:&ensp; 언제 사용할까?
* 데이터를 입력된 순서대로 처리하는 경우

* BFS 구현 시

<br/>

:bulb:&ensp; 큐 자료형을 사용하는 대표적인 문제

* BFS 문제

* 콜센터 대기 순서

* 프로세스 관리

<br/>

### 1. 구현

#### :pushpin:&ensp; Python 구현

* [List를 활용한 구현](./queue/python/queue_list.md)

* [collections.deque 모듈 사용 방법 및 Operation 별 Time Complexity 정리](./queue/python/queue_deque.md)

* 선형 큐 구현

* 순환 큐 구현

<br/>

---
<h2 id="ds-5">5️⃣  Tree</h2>

### 0. Overview

계층적 관계(Hierarchical Relationship)을 표현하는 비선형 자료구조. 파일시스템과 같이 큰 데이터를 처리하는 소프트웨어들은 대부분 빠른 탐색을 위해, 데이터를 트리 자료구조 형태로 저장하여, 이진 탐색과 같은 탐색 기법을 활용함. 트리 구현을 위해서는 회로 Cycle이 존재하지 않아야 함.

|Tree Terminology       |Description|
|-                      |-          |
|Node                   |트리를 구성하는 각각의 요소를 의미. 트리 자료구조의 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체를 뜻함.|
|Edge                   |노드와 노드를 연결하는 선을 의미.|
|Root Node              |트리 구조에서 최상위에 위치한 노드를 의미.|
|Terminal Node(=Leaf Node, 단말 노드) |하위에 다른 노드가 연결되어있지 않은 노드를 의미.|
|Internal Node(내부노드, 비단말 노드)    |단말 노드를 제외한 모든 노드를 의미. 루트노드를 포함함.|
|Sub Tree               |트리 자료구조는 트리 자료구조의 일부를 떼어내도 트리 구조를 유지하며, 뗴어낸 트리를 서브 트리라고 함.|
|Left Chile Node        |왼쪽 서브 트리의 노드를 의미.|
|Right Chile Node       |오른쪽 서브 트리의 노드를 의미.|
|Parent Node            |그 노드를 자식으로 하는 노드를 의미.|
|Sibling Node           |부모가 같은 두 노드를 의미.|
|Degree(노드의 차수)       |자식의 수|
|Leaf Node              |차수가 0인 노드. 다시말해 자식이 없는 노드를 의미.|
|Path                   |-|
|Length                 |경로를 포함하는 방향 간선의 수. 시작점과 출발점이 같은 경로의 길이는 0|
|Ancestor Node          |두 노드 사이에 양수 길이의 경로가 존재한다면, 시작점 노드를 도착점 노드의 조상 노드라고 함.|
|Descendant Node        |두 노드 사이에 양수 길이의 경로가 존재한다면, 도착점 노드를 시작점 노드의 자손 노드라고 함.|
|Depth                  |노드의 깊이를 의미하며, 루트 노드에서 자신까지 가는 경로의 길이. 루트 노드의 깊이는 0.|
|Level                  |루트 노드에서 자신까지 가는 경로의 길이 + 1.이 때, 루트노드의 레벨은 1이 됨. 간혹 트리의 특정 깊이를 가지는 노드의 집합을 레벨이라고 하기도 함. `Level = Depth` or `Level = Depth + 1`이 혼용되어 사용되는 듯.|
|Hight                  |특정 노드와 단말 노드 사이의 경로의 최대 길이.|
|Size                   |자기 자신 및 모든 자손 노드의 수.|

:bulb:&ensp; 트리 용어는 잘 표준화되어있지 않기 때문에, 문헌마다 차이가 있을 수 있음

<br/>

### 1. Tree의 종류

* Binary Tree(이진 트리)

    > `루트 노드를 중심으로 두개의 서브 트리`로 나뉘어지고, `나뉘어진 두 서브 트리 또한 모두 이진 트리인 트리`의 형태를 이진 트리라고 함. 이처럼 이진 트리는 재귀적으로 정의되기 때문에, 재귀적 정의 과정이 Leaf Node에 도달했을 때에도 정의를 만족하기 위해, `공집합 또한 이진 트리`로 포함하여야 함.


    배열로 구성된 이진 트리는 `노드의 갯수가 n개`이고, `root가 0이 아닌 1`에서 시작할 때, 다음과 같은 특징이 성립함.

    |i'th Node          |Parent     |
    |-                  |-          |
    |Parent Node        |`i // 2`    |
    |Left Child Node    |`i * 2`    |
    |Right Child Node   |`i * 2 + 1`|


    :bulb:&ensp; `i = 4`일 때의 예시는 다음과 같다.

    |Array Index|0|1|2|3|`4`|5|6|7|8|9|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    ||Unused :x:|Root Node|Parent Node|-|`i th Node`|-|-|-|Left Child Node|Right child Node|
    ||-|-|`i // 2`|-|`i`|-|-|`i * 2`|`i * 2 + 1`|

<br/>

* Perfect Binary Tree(포화 이진 트리)

    > 트리의 모든 내부 노드가 두개의 자식 노드를 가지며, 모든 Leaf Node가 동일한 깊이 또는 레벨을 갖는 트리. 다시 말해, `모든 리프 노드의 레벨이 동일`하고, `모든 레벨이 꽉 찬 이진 트리`를 의미.

<br/>

* Complete Binary Tree(완전 이진 트리)

    > 부모 노드, 왼쪽 자식 노드, 오른쪽 자식 노드 순으로 채워지는 이진 트리. 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 노드들이 왼쪽부터 순서대로 채워져 있는 노드의 형태를 의미.

<br/>

* Full Binary Tree(정 이진 트리) or Proper Binary Tree(적정 이진 트리)

    > 모든 노드가 0개 또는 2개의 자식 노드를 갖는 트리를 의미. (자식 노드의 갯수가 홀수 개가 아니여야 함.)

<br/>

* Binary Search Tree(BST)

    > 효율적인 탐색을 위해서는 `데이터를 찾는 방법` 뿐만 아니라 `데이터를 저장하는 방법` 또한 중요하게 고려해야함. `Binary Search Tree(이진 탐색 트리)`는 이진트리의 일종으로, 특정 규칙에 따라 데이터를 저장하고, 이 규칙을 이후 데이터 탐색 시 활용하는 형태의 자료구조.

    * 규칙 1. 이진 탐색 트리에서 노드에 저장된 키는 유일해야 함.

    * 규칙 2. 부모 노드의 키가 왼쪽 자식 노드의 키보다 커야 함.

    * 규칙 3. 부모 노드의 키보다 오른쪽 자식 노드의 키가 커야 함.

    * 규칙 4. 특정 노드를 기준으로 왼쪽과 오른쪽의 서브트리 또한 이진 탐색 트리인 조건을 만족해야 함.

    <br/>

    :pushpin:&ensp; 이진 탐색 트리의 탐색 연산의 시간복잡도

    이진 탐색 트리의 탐색 연산은 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(h)%5C%20%5Capprox%5C%20O(%5Clog%7B%7D%7Bn%7D)" />의 시간 복잡도를 가짐. 이는 트리의 높이가 하나씩 증가될수록, 추가되는 노드의 수가 두 배씩 증가하기 때문.

    이와 같은 이진 탐색 트리는 `Skewed Tree(편향 트리)`가 될 수 있음. 저장 순서에 따라 계속 한 쪽으로만 노드가 추가되는 경우가 발생하기 때문. 이 경우, 성능에 영향을 미치게 되며, 탐색의 Worst Case가 되고 시간 복잡도는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />이 됨.

    이처럼 배열보다 많은 메모리를 사용하며 데이터를 저장했지만 탐색에 필요한 시간 복잡도가 같게 되는 비효율적인 상황이 발생함. 이를 해결하기 위해 `Rebalancing 기법`이 등장함. `균형을 잡기 위한 트리 구조의 재조정`을 Rebalancing이라 하며, 이 기법을 구현한 트리에는 여러 종류가 존재하는데, 그 중에서 하나가 `Red-Black Tree`.

    <br/>

    :bulb:&ensp; 코딩테스트에서의 이진 탐색 트리 문제

    > 사실 코딩테스트에서는 문제 해결을 위해 필수적으로 이진 탐색 트리 자료구조를 구현해야하는 문제는 출제 빈도가 높지 않음.

<br/>

* Red Black Tree

    > 

<br/>

* Balanced Binary Tree(균형 이진 트리)

    >

<br/>

### 2. 트리의 탐색/순회(Tree Traversal)

이진트리 및 전반적인 트리 구조에서 각가의 노드를 정확히 한 번만, 체계적으로 방문하는 과정을 말함. Tree Traversal 방식은 노드를 방문하는 순서에 따라 다음과 같이 분류됨. 아래의 트리 순회 방식 각각에 대한 설명은 이진 트리를 기준으로 작성되었지만, 다른 트리의 형태에도 일반화가 가능함.

|Tree Traversal         |Description|
|-                      |-          |
|in-order(중위 순회)      |왼쪽 자식 노드(L), 내 노드(P), 오른쪽 자식 노드(R) 순서로 방문.|
|pre-order(전위 순회)     |내 노드(P), 왼쪽 자식 노드(L), 오른쪽 자식 노드(R) 순서로 방문.|
|post-order(후위 순회)    |왼쪽 자식 노드(L), 오른쪽 자식 노드(R), 내 노드(P) 순서로 방문.|
|level-order(레벨 순회)   |내 노드(P)를 방문하고, 내 노드로부터 노드의 깊이가 낮은 순서대로 노드를 방문하는 방식.(`Depth = [0, 1, 2, ..., N(Depth)]`)|

<br/>

### 3. 구현

#### :pushpin:&ensp; Python 구현

* Binary Search Tree 구현

* 주어진 트리가 이진트리인지 여부를 확인하는 알고리즘 구현

<br/>

---
<h2 id="ds-6">6️⃣  Heap</h2>

<br/>

---
<h2 id="ds-7">7️⃣  Hash Table</h2>

<br/>

---
<h2 id="ds-8">8️⃣  Graph</h2>

### 1. Python 

* [인접행렬 구현](./graph/python/adjacent_matrix.md)

* [인접 리스트 구현](./graph/python/adjacent_list.md)

* [간선리스트 구현](./graph/python/edge_list.md)

### 2.  Edge Cases

<br/>

---
<h2 id="ds-9">9️⃣  Set</h2>

### 0. Overview

`집합(Set)`은 `원소(Member)`라는 구별되는 객체들이 연관되어 모인 것을 말하며, `서로 다른 연관된 원소`들의 `순서 없는` 모임이다.

### 1. Python

* [set 자료형](./set/python/set.md)