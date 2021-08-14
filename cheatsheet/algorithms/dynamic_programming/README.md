# Dynamic Programming

## :one:&ensp; Dynamic Programming 이란?

복잡한 문제를 여러 개의 하위 문제(sub-problem)으로 나누어 해결하는 방식.

DP는 다음 두 가지 방식으로 구현 가능함.

* top-down: 문제를 여러 개의 하위 문제(sub-problem)을 나누고, 하위 문제에서 구한 답을 결합하여 최종적으로 최적해를 구하는 방식.

    * memoization: 하위 문제에서 구한 답을 저장해놨다가 이후에 값을 계산하지 않고 가져다가 쓰는 방식.

* bottom-up: top-down 방식과 달리 하위 문제들로 상위 문제의 최적해를 구하는 방식.

<br/>

---
## :two: Dynamic Programming의 접근 방법

1. 모든 답을 만들어 보고 그 중 최적해의 점수를 반환하는 완전 탐색 알고리즘을 설계함.

2. 전체 답의 점수를 반환하는 것이 아니라, 앞으로 남은 선택들에 해당하는 점수만을 반환하도록 부분 문제의 정의를 변경함.

3. 재귀 호출의 입력 이전 선택에 대한 정보가 있다면, 꼭 필요한 것만을 남기고 줄임.

4. 입력이 배열이거나 문자열인 경우, 가능하다면 적절한 변환을 거쳐 메모이제이션 할 수 있도록 조정함.

5. 메모이제이션을 적용함.

<br/>

---
## Reference

* https://hongjw1938.tistory.com/47

* 동빈북

* https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Algorithm