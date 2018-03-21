/* 
 * # 12813 : 이진수 연산
 * - 문제
 * 총 100,000 비트로 이루어진 이진수 A와 B가 주어진다. 
 * 이 때, A & B, A | B, A ^ B, ~A, ~B를 한 값을 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 이진수 A, 둘째 줄에 이진수 B가 주어진다. 
 * 두 이진수의 길이는 모두 100,000이다. 예제의 경우에만 길이가 10이며, 
 * 예제는 채점하지 않는다.
 * 
 * - 출력
 * 첫째 줄부터 한 줄에 하나씩 차례대로 A & B, A | B, A ^ B, ~A, ~B를 출력한다.
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
#include <bitset>
#include <string>

using namespace std;

#define BIT_LEN 100000

int main()
{
    string input;   
    cin >> input;
    bitset<BIT_LEN> b1(input);
    
    cin >> input;
    bitset<BIT_LEN> b2(input);
    
    cout << (b1 & b2) << '\n';
    cout << (b1 | b2) << '\n';
    cout << (b1 ^ b2) << '\n';
    cout << (~b1) << '\n';
    cout << (~b2) << '\n';

}