/* 
 * # 6588 : 골드바흐의 추측
 * - 문제
 * 
 * 
 * - 입력
 * 
 * 
 * - 출력
 * 
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
 * 백준 gist 풀이
 * 
 * 짝수 = 두 소수의 합
 * (1)짝수 - 위의 두 소수 중 하나의 소수 = (2)나머지 "소수"
 * 따라서 (1)이 소수인지 검사해주면 되는 것
*/

// Solve 1
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000000;
// true  : not prime, deleted number 
// false : prime, not (yet) deleted number
int prime[MAX]; // to store prime number
int pn;
int check[MAX]; // to store the state of number which already checked

void seiveOfEranthoses();

int main()
{
    ios_base::sync_with_stdio( false ), cin.tie( NULL );

    seiveOfEranthoses();
    while(1){
        int n; cin >> n;
        if(n == 0) break;

        // exclude prime[0] = 2 
        for(int i=1; i<n; i++){
            // even number - prime number which is odd numver = other prime number which is odd numver
            if(check[n - prime[i]] == false){
                cout << n << " = " << prime[i] << " + " << n - prime[i] << '\n';
                break; // to get only max result
            }
        }
    }
}

void seiveOfEranthoses(){
    // sieve of eranthoses
    for (int i = 2; i <= MAX; i++)
    {
        if (check[i] == false)
        {
            // store current number to prime array
            prime[pn++] = i;

            // check the multiple of i
            for (int j = i + i; j < MAX; j += i)
            {
                check[j] = true;
            }
        }
    }
}