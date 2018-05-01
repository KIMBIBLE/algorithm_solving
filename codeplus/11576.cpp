/* 
 * # 11576 : Base Conversion
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
 * m자리 A 진법(1 ≤ m ≤ 25)을 B 진법으로 변환하는 문제.
 * 
 * A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 2^20보다 작다.
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

int AToTenConversion(vector<int> &, int a);
void TenToBConversion(int n, int b);
int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int a, b; cin >> a >> b;
    int m; cin >> m;
    vector<int> x(m);
    for(int i=0; i<m; i++){
        cin >> x[i];
        x[i] - '0';
    }

    int num = AToTenConversion(x, a);
    if(num == 0){
        cout << 0;
    }
    else{
        TenToBConversion(num, b);
    }
}

int AToTenConversion(vector<int> &x, int a){
    int len = x.size();
    int base = 1;
    int res = 0;

    for(int i=len-1; i>=0; i--){
        res += x[i] * base;
        base *= a;
    }

    return res;
}

void TenToBConversion(int n, int b){
    if(n==0) return;

    int r = n%b;
    TenToBConversion(n/b, b);
    if(r){ // if remainder exists
        cout << r << ' ';
    }
    else{
        cout << 0 << ' ';
    }
}