# Hashing with Open Addressing(개방 주소법)

## Table of Contents

본 문서에서는 다음의 내용을 중점으로 다룬다.

1. <a href="#sec_01">Open Addressing 기법을 활용하여 Hash Table을 관리하는 방법</a>

2. <a href="#sec_02">Open Addressing에서 Probing(탐사) 방법</a>

3. <a href="#sec_03">Open Addressing을 활용할 때, 삽입/삭제/탐색 연산의 시간 복잡도</a>

<br/>

---
<h2 id="sec_01">1️⃣&ensp; What is Open Addressing?</h2>

Open Addressing(Closed Hashing)은 해시 테이블 자료구조에서 collision을 해결하기 위한 방법이다. Open Addressing은 삽입/삭제/탐색을 수행하기 위해, hash collision 발생 시 해시 테이블 내 새로운 주소(해시 값)을 찾는 Probing(탐사) 과정을 추가적으로 수행하는 방식을 통해 collision을 해결한다.

해시 값을 바로 해시 테이블 내 버킷의 주소로 활용하는 naive approach와 비교했을 때, Open Addressing에서는 해시 값이 그대로 해시 테이블 내 버킷의 주소로 매핑되는 것이 아니라 x칸만큼(Probing 종류에 따라 달라짐) 떨어진 곳에 저장 될 수 있다.

<div align="center">
    <img width="60%" src="../../figure/open_addressing(linear_probing).png">
    <a href="https://en.wikipedia.org/wiki/Open_addressing">https://en.wikipedia.org/wiki/Open_addressing</a>
</div>

<br/>

### **1. Open Addressing을 사용하는 Hash Table의 Operations**

|Operation|Descriptions|
|-|-|
|`Insert(k)`|빈 슬롯을 찾을 때 까지 계속 탐색함. 만약 빈 슬롯이 발견되면 `k`를 삽입함.|
|`Search(k)`|슬롯의 키가 `k`와 같지 않거나, 빈 슬롯에 도달할 때 까지 탐색을 수행함.|
|`Delete(k)`|삭제된 키에 해당되는 슬롯에 삭제된(`DELETED`) 슬롯이라고 마킹함. 이는 단순히 키를 삭제하게되면 `Search` 동작에 영향을 줄 수 있기 때문.|

<br/>

### **2. Open Addressing 예시**

다음 조건에 따라 Open Addressing 방식으로 `해시 테이블(T)`에 키를 순차적으로 저장하고자 할 때, 각각의 단계에 대해 알아보자.

* <img src="https://chart.apis.google.com/chart?cht=tx&chl=h(k)%5C%20%3D%5C%20k%5C%20%5Cbmod%5C%207" />로 정의.

* `key(k)`는 `50, 700, 76, 85, 92, 73, 101` 순서로 저장된다.

* `Linear Probing(선형 탐사)` 방식을 활용: Collision 발생 시, Collision이 발생한 해시 테이블의 슬롯보다 `1칸 뒤`에 데이터를 저장함.

<div align="center">
    <img width="60%" src="../../figure/open_addressing_steps.png">
    <a href="https://www.geeksforgeeks.org/hashing-set-3-open-addressing/">https://www.geeksforgeeks.org/hashing-set-3-open-addressing/</a>
</div><br/>

|Setps|Descriptions|Collision|
|-|-|:-:|
|1. Initial Empty Table|크기가 7인 해시 테이블(T)의 초기 상태.|X|
|2. Insert(50)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=50%5C%20%5Cbmod%5C%207%5C%20%3D%5C%201" />로 `T[1]`에 `50`이 저장됨.|X|
|3. Insert(700)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=700%5C%20%5Cbmod%5C%207%5C%20%3D%5C%200" />으로 `T[0]`에 `700`이 저장됨.|X|
|4. Insert(76)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=76%5C%20%5Cbmod%5C%207%5C%20%3D%5C%206" />으로 `T[6]`에 `76`이 저장됨.|X|
|5. Insert(85)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=85%5C%20%5Cbmod%5C%207%5C%20%3D%5C%201" />으로 `T[1]`에 이미 데이터가 저장되어 있음. Collision이 발생하였기 때문에, 빈 슬롯을 찾을 때 까지 1칸씩 계속 탐색 수행.|O|
|6. Insert(92)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=92%5C%20%5Cbmod%5C%207%5C%20%3D%5C%201" />으로 `T[1]`에 이미 데이터가 저장되어 있음. Collision이 발생하였기 때문에, 빈 슬롯을 찾을 때 까지 1칸씩 계속 탐색 수행. `T[2]`에도 데이터가 있기 때문에 `T[3]` 위치에 `92` 삽입.|O|
|7. Insert(73)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=73%5C%20%5Cbmod%5C%207%5C%20%3D%5C%203" />으로 `T[3]`에 이미 데이터가 저장되어 있음. 따라서 `T[4]`의 위치에 `92` 삽입.|O|
|7. Insert(101)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=101%5C%20%5Cbmod%5C%207%5C%20%3D%5C%203" />으로 `T[3]`에 이미 데이터가 저장되어 있음. 따라서 `T[5]`의 위치에 `101` 삽입.|O|

<br/>

---
<h2 id="sec_02">2️⃣&ensp; Probings(탐사)</h2>

Probing(탐사)이란 삽입/삭제/탐색을 수행하기 위해 해시 테이블 내 새로운 주소(해시 값)을 찾는 과정을 의미한다. 

<br/>

---
<h2 id="sec_03">3️⃣&ensp; Time Complexity</h2>

