/* 
 * # 1373 : 2진수 8진수
 * - 문제
 * 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.
 * 
 * - 출력
 * 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
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
    string x, s;
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    cin >> x;

    int m, n, i = 0;
    m = x.length();
    n = m % 3;
    if(n == 1){
        s += to_string(x[i++] - '0');
    } 
    else if(n == 2){
        s += to_string(2*(x[i++] -'0') + x[i++] - '0' );
    } else{;}

    while(i<m)
        s += to_string(4*(x[i++] -'0') + 2*(x[i++] -'0') + x[i++] - '0' );
    cout << s;

}