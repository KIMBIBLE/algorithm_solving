# Python Built-in List 자료형의 Operation 별 시간복잡도 분석

The Average Case assumes parameters generated uniformly at random.

Internally, a list is represented as an array; `the largest costs` come from `growing beyond the current allocation size (because everything must move)`, or from `inserting or deleting somewhere near the beginning (because everything after that must move)`. If you need to add/remove at both ends, consider using a collections.deque instead.

<br/>

## Time Complexity

|Operation  |Average Case   |Amortized Worst Case   |
|:-:        |:-:            |:-:                    |
|Copy       |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(N)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Append(1)  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|Pop Last   |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|Pop intermediate[2]|<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Insert     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Get Item   |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|Set Item   |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|
|Delete Item|<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Iteration  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Get Slice  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(k)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k)" />|
|Del Slice  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n)" />|
|Set Slice  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(k%2Bn)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k%2Bn)" />|
|Extend[1]  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(k)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(k)" />|
|Sort       |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n%5Clog_%7B%7D%7Bn%7D)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(n%5Clog%7B%7D%7Bn%7D)" />|
|Multiply   |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(nk)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(nk)" />|
|x in s     |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />||
|min(s), max(s)|<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(n)" />||
|Get Length |<img src="https://chart.apis.google.com/chart?cht=tx&chl=\Theta(1)" />|<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(1)" />|

---
## 참고

* https://wiki.python.org/moin/TimeComplexity