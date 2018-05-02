/* 
 * # 10989 : 수 정렬하기 3
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
 * 메모리 용량 제한이 8M : 8,000,000 byre
 * 
*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

const int MAX = 10000;
int x[MAX + 1];

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int n; cin >> n;
    for(int i=0; i<n; i++){
        int tmp; cin >> tmp;
        x[tmp]++;
    }

    for(int i=1; i<=MAX; i++){
        if(x[i] > 0){
            for(int j=1; j<=x[i]; j++){
                cout << i << '\n';
            }
        }
    }

}