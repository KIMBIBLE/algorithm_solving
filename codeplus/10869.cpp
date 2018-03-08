/* 
 * # 10869 : 사칙연산
 * - 문제
 * 두 자연수 A와 B가 주어진다. 이 때, 
 * A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
 * 
 * - 입력
 * 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
 * 
 * - 출력
 * 첫째 줄에 A+B, 둘째 줄에 A-B, 
 * 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 입력 후 사칙연산 결과 출력.
 * 람다 함수 연습. 
 * 
 * - 생각
 * 
 * 
 * SOLVE 1> 
 * 백준 solve
 * 
*/

// Solve 1
#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int main()
{
    int A, B;
    cin >> A >> B;
    
    vector <function<int(int, int)> > calc;
    calc.push_back([](int x, int y){return x+y;});
    calc.push_back([](int x, int y){return x-y;});
    calc.push_back([](int x, int y){return x*y;});
    calc.push_back([](int x, int y){return x/y;});
    calc.push_back([](int x, int y){return x%y;});

    for(auto &f:calc)
    {
        cout << f(A,B) << endl;
    }
}