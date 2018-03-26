/* 
 * # 11655 : ROT13
 * - 문제
 * ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
 * 예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 
 * "Onrxwbba Bayvar Whqtr"가 된다. ROT13으로 암호화한 내용을 
 * 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다. 
 * 앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 
 * 적용하면 "Baekjoon Online Judge"가 된다.
 * 
 * ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 
 * 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다. 
 * 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.
 * 
 * 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 
 * 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 
 * 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.
 * 
 * - 출력
 * 첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 경계값을 넘어가면 rotate하는 문제.
 * 이런건 ++를 반복하면서 경계값을 넘어가나 체크해주는 방법을
 * 사용해도 되지만 보통 한줄로 줄일 수 있는 수식이 존재하는 경우가 많다.
 * 
 * 결과 = 기준값 + mod 결과
 * mod 결과 = (현재 값 - 기준값 + 변화값) % base 
 * 'a' + (now -'a'+13)mod26
 * 'A' + (NOW -'A'+13)mod26
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

const char ROT_NUM = 13;

bool isSmallAlpha(char);
bool isBigAlpha(char);

int main()
{
    string s, s2;
    getline(cin, s);

    for(auto it=s.begin(); it != s.end(); ++it){
        if(isSmallAlpha(*it)){
            *it = 'a' + (*it - 'a' + ROT_NUM) % 26;
        }
        else if(isBigAlpha(*it)){
            *it = 'A' + (*it - 'A' + ROT_NUM) % 26;
        }
        else{;}
    }
    cout << s;
}


bool isSmallAlpha(char ch)
{
    if('a' <= ch && ch <= 'z'){
        return true;
    }
    return false;
}

bool isBigAlpha(char ch)
{
    if('A' <= ch && ch <= 'Z'){
        return true;
    }
    return false;
}
