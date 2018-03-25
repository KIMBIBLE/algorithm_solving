/* 
 * # 2750 : 수 정렬하기
 * - 문제
 * N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 수의 개수 N(1<=N<=1,000)이 주어진다. 
 * 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절대값이 
 * 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
 * 
 * - 출력
 * 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
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
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector <int> v;
    int x;
    scanf("%d", &x);
    for(int i=0; i<x; i++){
        int n;
        scanf("%d", &n);
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    for(int x : v){
        printf("%d\n", x);
    }
}