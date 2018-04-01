/* 
 * # 9095 : 1, 2, 3 더하기
 * - 문제
 * 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 총 7가지가 있다.
 * 
 * 1+1+1+1
 * 1+1+2
 * 1+2+1
 * 2+1+1
 * 2+2
 * 1+3
 * 3+1
 * 
 * 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 
 * 구하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 
 * 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. 
 * n은 양수이며 11보다 작다.
 * 
 * - 출력
 * 각 테스트 케이스마다, n을 1,2,3의 합으로 나타내는 방법의 수를 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * d[n] = n을 1, 2, 3의 합으로 나타내는 방법의 수 => 부분문제
 * d[n] = d[n-1] + d[n-2] + d[n-3]
 * 
 * 부분 문제의 최솟값 : d[4] = d[3] + d[2] + d[1]
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
using namespace std;

int solve(vector<int> &, int);

int main()
{
    int t, n;
    cin >> t;
    while(t--){
        cin >> n;
        vector<int> d(n+1, 0);
        cout << solve(d, n) << '\n';
    }
}

int solve(vector<int> &d, int n)
{
    if(n <= 2) return n;
    if(n == 3) return 4;
    if(d[n] > 0) return d[n];

    d[n] = solve(d, n-1) + solve(d, n-2) + solve(d, n-3);
    return d[n];
}