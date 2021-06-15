# Sort

## 소팅 알고리즘의 종류

### 1. 선택정렬

> 최소값 찾기(선택)를 반복하는 알고리즘. 무작위 데이터 리스트에서 가장 작은 값을 선택하여 리스트의 맨 앞의 요소와 교환함. 이후 선택이 완료된 데이터 리스트의 맨 앞 요소를 제외한 나머지 데이터들에 대해 최소값 찾기를 반복함.



### 2. 삽입정렬


### 3. 퀵정렬


### 4. 계수정렬


---
## 소팅 알고리즘의 시간복잡도 비교

각 정렬에 소요되는 비교 횟수를 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C" />라고 했을 때, 비교 횟수의 평균은 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" />, 최대는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" />, 최소는 <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" />으로 표기함. 

|알고리즘|<img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bave%7D" />| <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmax%7D" /> | <img src="https://chart.apis.google.com/chart?cht=tx&chl=C_%7Bmin%7D" /> |
|-|-|-|-|
|선택 정렬|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7BO_n%7D%5E2" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7BO_n%7D%5E2" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=%7BO_n%7D%5E2" />|

### 1. 선택정렬

<img src="https://chart.apis.google.com/chart?cht=tx&chl=%5C%5BC_%7Bmin%7D%5C%20%3D%5C%20C_%7Bave%7D%5C%20%3D%5C%20C_%7Bmax%7D%5C%20%3D%5C%20%5C%20%5Csum_%7Bi%3D1%7D%5E%7BN-1%7D%5C%20N%5C%20-%5C%20i%5C%20%5C%20%3D%5C%20%5Cfrac%7BN(N%5C%20-%5C%201)%7D%7B2%7D%5C%20%3D%5C%20O(N%5E1)%5C%5D" />
