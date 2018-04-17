/* 
 * # 10430 : 나머지
 * - 문제
 * 두 수의 합과 곱에 대한 모듈러 연산의 결합법칙이 성립하는지에 대한 문제
 * 
 * - 입력
 * 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
 * 
 * - 출력
 * 첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 
 * 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * dp 문제같이 계산하는 정수 범위가 저장 범위를 초과하는 경우 사용하면
 * 편할 듯 하다.
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
    int a, b, c;
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    cin >> a >> b >> c;
    cout << (a + b) % c << '\n';
    cout << (a % c + b % c) % c << '\n';
    cout << (a * b) % c << '\n';
    cout << (a %c * b % c ) % c << '\n';
}