/* 
 * # 1929 : 소수 구하기
 * - 문제
 * M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
 * 시간제한 : 2초
 * 
 * - 입력
 * 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1≤M≤N≤1,000,000)
 * 
 * - 출력
 * 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * root n까지 나누는 방법으로 소수를 구하게 되면 nlogn 시간 복잡도.
 * 최악의 경우인 m=1, n = 1,000,000 인 상황을 가정했을 때의 복잡도는
 * 1,000,000 * 1,000 = 1,000,000,000(10억)으로 시간이 10초가량 소요 됨.
 * 
 * 문제의 제약조건인 2초 안에 들어오기 위해서는 다른 방법을 사용해야함.
 * 이 때 사용할 수 있는 알고리즘은 에라토스테네스의 채가 있음.
 * Time Complexity : nloglogn = 1,000,000 * 10 root 10 = 10,000,000 * root 10
 * n이 1억정도일 때 소요 시간을 1초로 가정하면 0.3초 정도 시간정도가 걸릴 듯.
 * 
 * - 생각
 * 에라토스테네스의 채 : 소수 판별을 위해 나눌 수는 root(n) 까지인 것은 동일하나
 * 해당 수가 소수일 때마다 해당 소수의 배수를 없애 주는 방식으로 중복 검사 비율을 감소.
 * 
 * SOLVE 1> 
 * 
 * 
*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n);

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );
    int m, n; cin >> m >> n;
    // true : prime, false : compound
    vector<bool> x(n+1, true);
    x[0] = x[1] = false;

    for(int i=2; i*i<=n; i++){
        if(isPrime(i)){
            for(int j=i*2; j<=n; j+=i){
                x[j] = false;
            }
        }
    }

    for(int i=m; i<=n; i++){
        if(x[i]) cout << i << '\n';
    }

}

bool isPrime(int n)
{
    if(n<2) return false;

    for(int i=2; i*i<=n; i++){
        if(n%i == 0) return false;
    }

    return true;
}