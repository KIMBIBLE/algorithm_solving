/* 
 * # 2609 : 최대공약수와 최소공배수
 * - 문제
 * 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
 * => 곱의 최대도 100,000,000 이므로 LCM의 경우의 결과 또한 int 자료형으로 표현가능
 * 
 * - 출력
 * 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를,둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
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
 * gcd : euclidian algorithm
 * lcm : a * b / gcd(a, b)
 * 
*/

int gcd(int a, int b);
int lcm(int a, int b);

// Solve 1
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    cin >> a >> b;
    cout << gcd(a, b) << '\n' << lcm(a, b);
}


int gcd(int a, int b)
{
    if(b>a) swap(a,b);
    if(b == 0) return a;
    gcd(b, a%b);
}

int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}