/* 
 * # 1676 : 팩토리얼 0의 개수
 * - 문제
 * N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
 * 
 * - 출력
 * 첫째 줄에 구한 0의 개수를 출력한다.
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

    int cnt = 0;
    int x = 1;
    for(int i=2; i<=n; i++){
        int x = i;
        while (x % 5 == 0){
            x /= 5;
            cnt++;
        }
    }
    cout << cnt;
}