# 소팅 알고리즘의 시간복잡도/공간복잡도 비교

<table>
    <thead>
        <tr>
            <th>Algorithms</th>
            <th colspan="3" align="center">Time Complixity</th>
            <th colspan="3" align="center"><img src="https://chart.apis.google.com/chart?cht=tx&chl=times(n)_%7Bsec%7D" /></th>
            <th colspan="2" align="center">Space Complexity</th>
        </tr>
        <tr>
            <th>&nbsp;</th>
            <th>Worst<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=O" /> </th>
            <th>Best<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega" /></th>
            <th>Average<br/><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta" /></th>
            <th>N=100</th>
            <th>N=1,000</th>
            <th>N=10,000</th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=mem_%7Bworst%7D" /></th>
            <th><img src="https://chart.apis.google.com/chart?cht=tx&chl=mem_%7Bavg%7D" /></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>선택 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /></td>
            <td>0.0123</td>
            <td>0.354</td>
            <td>15.475</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>삽입 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n^2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>퀵 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>0.00156</td>
            <td>0.00343</td>
            <td>0.0312</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(%5Clog_%7B%7DN)" /></td>
        </tr>
        <tr>
            <td>내장 정렬 라이브러리</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7Dn)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7Dn)" /></td>
            <td>0.00000753</td>
            <td>0.0000365</td>
            <td>0.000248</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>계수 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%2Br)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%2Br)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%2Br)" /></td>
        </tr>
        <tr>
            <td>버블 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N^2)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(N)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(N%5E2)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>병합 정렬</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5Clog_%7B%7D%5C%20n)" /></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /></td>
            <td>-</td>
        </tr>
        <tr>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
            <td>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</td>
        </tr>
    </tbody>
</table>

* `n`: 데이터의 갯수, `r` 정렬될 수의 범위.

* 각 소팅 알고리즘의 시간 측정 환경: Intel(R) Core(TM)i7-7500U CPU @ 2.70GHz. 2 Core 환경

* [더 많은 정렬 알고리즘과 각 알고리즘의 분류](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

* 파이썬의 built-in sort 함수는 [Timsort 알고리즘](https://en.wikipedia.org/wiki/Timsort)을 사용함.

  * 내부적으로 C 기반으로 구현되었고, 최적화 테크닉이 들어가 훨씬 빠르게 동작함.

<br/>

---
## 1. 선택정렬

### ***Worst-Case Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" /> 번 swap 수행.

### ***Best-Case  Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(1)" /> 번 swap 수행.

### ***Average    Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n)" /> 번 swap 수행.

<br/>

---
## 2. 삽입정렬

### ***Worst-Case Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" /> 번 swap 수행.

### ***Best-Case  Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(1)" /> 번 swap 수행.

### ***Average    Performance***

* 비교 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 비교 동작 수행.

* Swap 연산: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5CTheta(n%5E2)" /> 번 swap 수행.


<br/>

---
## 3. 퀵정렬

### ***Worst-Case Performance***: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5E2)" />

### ***Best-Case  Performance***

* Simple Partition: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n%5Clog_%7B%7D%7Bn%7D)" />

* Three-way Partition and equal keys: <img src="https://chart.apis.google.com/chart?cht=tx&chl=%5COmega(n)" />

### ***Average    Performance***: <img src="https://chart.apis.google.com/chart?cht=tx&chl=n%5Clog%7B%7D%7Bn%7D" />

<br/>

---
## 4. 계수정렬

모든 데이터가 양의정수이고, 데이터 갯수가 `N`, 데이터 중 최대값의 크기가 `K`인 상태.

<br/>

### ***시간 복잡도***: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20%2B%5C%20K)" />
  
* 정렬 정보를 저장하는 배열에 데이터를 삽입하는 동작: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N)" />
  
* 정렬 정보를 저장하는 배열을 순차적으로 방문하는 동작: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(K)" />

<br/>

### ***공간 복잡도***: <img src="https://chart.apis.google.com/chart?cht=tx&chl=O(N%5C%20%2B%5C%20K)" />

<table>
<thead>
<tr>
<th>배열 크기</th>
<th>할당 메모리(MB)</th>
<th>할당 시간(sec)</th>
</tr>
</thead>
<tbody>
<tr>
<td>100,000(십만)</td>
<td>0.7MB</td>
<td>0.00007 sec</td>
</tr>
<tr>
<td>1,000,000(백만)</td>
<td>7MB</td>
<td>0.00128 sec</td>
</tr>
<tr>
<td>10,000,000(천만)</td>
<td>76MB</td>
<td>0.01291 sec</td>
</tr>
<tr>
<td>100,000,000(억)</td>
<td>762MB</td>
<td>0.60375 sec</td>
</tr>
</tbody>
</table>

```python
sys.getsizeof([0]*100000) // (2 ** 20)      # 십만, 0.7 MB, 0.00007 sec
sys.getsizeof([0]*1000000) // (2 ** 20)     # 백만,   7 MB, 0.00128 sec
sys.getsizeof([0]*10000000) // (2 ** 20)    # 천만,  76 MB, 0.01291 sec
sys.getsizeof([0]*100000000) // (2 ** 20)   # 일억, 762 MB, 0.60375 sec

[0 for _ in range(size)] # List Comprehension으로 생성할 경우 현저히 느려짐.
```

<br/>

---
## :three:&nbsp; 읽어볼만한 문서


* [What are Sorting Algorithms?](https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/): 각 정렬 알고리즘에 대한 시간/공간 복잡도 정리가 잘 되어있음.