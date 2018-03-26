/* 
 * # 11726 : 2*n 타일링
 * - 문제
 * 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
 * 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
 * 그림은 https://www.acmicpc.net/problem/11726 참조 
 * 
 * - 입력
 * 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
 * 
 * - 출력
 * 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * d[n] = 2*n 크기의 타일을 채우는 방법의 수
 * 부분문제를 구하기 위해 d[n]의 시점에서 이게 어떻게 만들어 졌나 생각해보자
 * d[n] = d[n-1] + d[n-2]가 나오게 되어있음.
 * 
 * 부분문제의 최소는 (d[3] = 3) = d[2] + d[1]이니까
 * d[1] = 1, d[2] = 2로 가정
 * 
 * - 생각
 * DP 알고리즘의 복잡도를 계산해보면,
 * 구하려는 부분문제의 갯수 : N
 * 각 부분문제의 복잡도 : O(1)
 * 총 O(N)이 나온다.
 * 
 * SOLVE 1> 
 * d[n] 메모시 % 10007 안해주면 안된다. long long도 인티져 오버플로우 남.
 * 
*/

// Solve 1
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> &, int);

int main()
{
    int n;
    cin >> n;
    vector<int> d(n+1, 0);
    cout << solve(d, n) % 10007;
}

int solve(vector<int> &d, int n)
{
    if(n == 1) return 1;
    if(n == 2) return 2;
    if(d[n] > 0) return d[n];

    d[n] = (solve(d, n-1) + solve(d, n-2))%10007;
    return d[n];
}