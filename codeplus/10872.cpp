/* 
 * # 10872 : 팩토리얼
 * - 문제
 * 0보다 크거나 같은 정수 N이 주어진다. 이 때, N!을 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
 * 
 * - 출력
 * 첫째 줄에 N!을 출력한다.
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
 * 
 * 
*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int n; cin >> n;

    int res = 1;
    for(int i=2; i<=n; i++){
        res *= i;
    }
    cout << res;
}