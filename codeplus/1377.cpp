/*
 * # 1377 : 버블소트
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
 * 버블소트
 *
 * - 생각
 *
 *
 * SOLVE 1>
 *
 *
*/

// Solve 1
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 500000;

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int n; cin >> n;
    // a.first : value
    // a.second : index before sore
    vector <pair<int, int>> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a.begin(), a.end());

    vector<int> x(n);
    for(int i=0; i<n; i++){
        x[i] = a[i].second - i;
    }


        cout << *max_element(x.begin(), x.end()) + 1 << endl;
}
