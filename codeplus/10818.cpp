/* 
 * # 10818 : 최소, 최대
 * - 문제
 * N개의 정수가 주어진다. 이 때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 
 * N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 
 * 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
 * 
 * - 출력
 * 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 
 * 
 * - 생각
 * 
 * 
 * SOLVE 1> 
 * pair의 iter에 접근할 때는 -> 이게 안되네;;;
 * '*res.first' 이런식으로 쓰자
 * 
*/

// Solve 1
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    auto res = minmax_element(a.begin(), a.end());
    cout << *res.first << ' ' << *res.second;
}