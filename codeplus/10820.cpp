/* 
 * # 10820 : 문자열 분석
 * - 문제
 * 문자열 N개가 주어진다. 이 때, 문자열에 포함되어 있는 
 * 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
 * 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
 * 
 * - 입력
 * 첫째 줄부터 N번째 줄까지 문자열이 주어진다. 
 * (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.
 * 
 * - 출력
 * 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 
 * 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
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
#include <string>
using namespace std;

int main()
{
    string s;
    while(getline(cin, s)){
        int lower = 0;
        int upper = 0;
        int num = 0;
        int space = 0;

        for(auto x : s){
            if(x >= 'a' && x <= 'z')
                lower++;
            else if(x >= 'A' && x <= 'Z')
                upper++;
            else if(x >= '0' && x <= '9')
                num++;
            else if(x == ' ')
                space++;
            else{;}
        }
        printf("%d %d %d %d\n", lower, upper, num, space);
    }
}