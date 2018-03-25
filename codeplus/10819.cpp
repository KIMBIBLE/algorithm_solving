/* 
 * # 10819 : 차이를 최대로
 * - 문제
 * N개의 정수로 이루어진 배열 A가 주어진다. 이 때, 배열에 들어있는 
 * 정수의 순서를 적절히 바꿔서 다음 식의 최대값을 구하는 프로그램을 작성하시오.
 * |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
 * 
 * - 입력
 * 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 
 * 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
 * 
 * - 출력
 * 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
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

#define non_exist -10000;

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int maxValue = non_exist;
    do{
        int sum = 0;
        for(int i=1; i<n; i++){
            sum += abs(a[i] - a[i-1]);
        }
        maxValue = max(maxValue, sum);
    }while(next_permutation(a.begin(), a.end()));
    cout << maxValue;
}