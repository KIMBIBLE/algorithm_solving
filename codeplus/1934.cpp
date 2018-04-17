/* 
 * # 1934 : 최소공배수
 * - 문제
 * 
 * 
 * - 입력
 * 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
 * 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
 * 
 * - 출력
 * 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 최소공배수 연산의 최대값이 int 자료형 범위 안에 들어옴.
 * 
 * - 생각
 * 
 * 
 * SOLVE 1> 
 * gcd 구현 -> 유클리드(시간복잡도 계산은?)
 * lcm 구현 -> a * b / gcd(a, b)
 * 
*/

// Solve 1

#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b);
int lcm(int a, int b);


int main()
{
    int t, a, b;
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    cin >> t;
    while(t--){
        cin >> a >> b;
        cout << lcm(a, b) << '\n';
    }
}

int gcd(int a, int b)
{
    if(b>a) swap(a, b);
    if(b == 0) return a;
    gcd(b, a%b);
}

int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}