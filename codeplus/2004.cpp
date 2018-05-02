/* 
 * # 2004 : 조합 0의 개수
 * - 문제
 * nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
 * 시간제한 : 2초
 * 
 * - 입력
 * 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
 * 
 * - 출력
 * 첫째 줄에 0의 개수를 출력한다.
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
1 2 : 1
3 4 : 2
5 6 7 8 : 4 
9 10 11 12 13 14 15 16 : 8

2^1 -> 1
2^2 -> 2
2^3 -> 3
...
2^a -> a

1 5 : 1
10 15 20 25 : 5


5^0 ~ 5^1 : 5^0
5^1 ~ 5^2 : 5^1

5^n ~ 5^n+1 : 5^n ( n: 0~)

nCm
   n!      : 1~n
---------
m! (n-m)!  : 1~m   +   1~n-m

5^n -1
-----
5 - 1

2^n -1
-----
2 - 1

*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int n, m; cin >> n >> m;
    pair<long long, long long> x, y;
    x = y = make_pair(0, 0);
    for (long long i=2; i<=n; i*=2) { x.first += n/i;}
    for (long long i=2; i<=n-m; i*=2) { x.first -=(n-m)/i;}
    for (long long i=2; i<=m; i*=2) { x.first -=m/i;}

    for (long long i=5; i<=n; i*=5) { x.second += n/i;}
    for (long long i=5; i<=n-m; i*=5) { x.second -=(n-m)/i;}
    for (long long i=5; i<=m; i*=5) { x.second -=m/i;}

    cout << min(x.first, x.second);
}