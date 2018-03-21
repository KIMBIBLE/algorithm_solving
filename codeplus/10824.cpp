/* 
 * # 10824 : 네 수
 * - 문제
 * 네 자연수 A, B, C, D가 주어진다. 이 때, A와 B를 붙인 수와 
 * C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.
 * 두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다. 
 * 즉, 20과 30을 붙이면 2030이 된다.
 * 
 * - 입력
 * 첫째 줄에 네 자연수 A, B, C, D가 주어진다. (1 ≤ A, B, C, D ≤ 1,000,000)
 * 
 * - 출력
 * A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 
 * - 생각
 * 
 * SOLVE 1> 
 * (1 ≤ A, B, C, D ≤ 1,000,000)
 * 자료형에 주의!!
 * int 쓰면 stoi에서 out_of_range 에러 터지면서 sys abort 터진다!
 * 
*/

// Solve 1
#include <iostream>
#include <string>
using namespace std;

int main()
{
    unsigned long long A, B, C, D;
    cin >> A >> B >> C >> D;

    auto con = [](unsigned long long  x, unsigned long long y){
        return stoull(to_string(x) + to_string(y));
    };
    
    string s = to_string(con(A,B) + con(C,D));

    printf("%s", s.c_str());
}