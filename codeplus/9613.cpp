/* 
 * # 9613 : gcd합
 * - 문제
 * 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 테스트 케이스의 개수 t (1 < t < 100)이 주어진다. 
 * 각 테스트 케이스는 한 줄로 이루어져 있고, 첫째 줄에는 수의 
 * 개수 n (1 < n < 100)가 주어지고, 다음에는 n개의 수가 주어진다. 
 * 입력으로 주어지는 수는 1000000을 넘지 않는다.
 * 
 * - 출력
 * 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 시간복잡도는 유클리드 알고리즘의 복잡도를 구하면 됨. 
 * => 정확하겐 모르지만 log(N)정도니까 앞에 100^2/2에 해당하는
 * 상수 곱이 붙어도 신경안써도 될 듯함.
 * 
 * 
 * - 생각
 * 알고리즘이 맞는 것 같고, 테스트 케이스도 어느 정도 잘 solve가 되는데
 * 문제가 틀리는 경우, 극소 극대 같은 예외값 처리에 문제가 있을 수도
 * 있지만, 결과 계산에서 자료형을 제대로 고려했나도 생각해줘야 한다.
 * 
 * SOLVE 1> 
 * 
 * 
*/

// Solve 1

#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b);

int main()
{
    int t, n;
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    cin >> t;
    while(t--){
        int n; cin >> n;
        vector<int> x(n);
        for(int i=0; i<n; i++){
            cin >> x[i];
        }

        long long sum = 0;
        for(int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++){
                sum += gcd(x[i], x[j]);              
            }
        }
        cout << sum << '\n';
    }

}

int gcd(int a, int b)
{
    if(b > a) swap(a, b);
    if(b == 0) return a;
    gcd(b, a % b);
}