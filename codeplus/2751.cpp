/* 
 * # 2751 : 수 정렬하기 2
 * - 문제
 * 
 * 
 * - 입력
 * 
 * 
 * - 출력
 * 
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
 * n이 100만이라 NlogN 알고리즘 사용하면 넉넉하게 1초 안에 들어올 듯
 * stl sort 사용
 * 
*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );

    int n; cin >> n;
    vector<int> x(n);
    for(int i=0; i<n; i++){
        cin >> x[i];
    }

    sort(x.begin(), x.end());
    for(auto &e : x){
        cout << e << '\n';
    }

}