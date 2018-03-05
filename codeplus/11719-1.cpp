/* 
 * # 11719 : 그대로 출력하기2
 * - 문제
 * 입력 받은 대로 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 
 * 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 
 * 각 줄은 100글자를 넘지 않으며, 빈 줄이 주어질 수도 있고, 
 * 각 줄의 앞 뒤에 공백이 있을 수도 있다.
 * 
 * - 출력
 * 입력받은 그대로 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 반복 입력 문제이기 떄문에 반복 종료 조건이 입력이 실패할 때가 될 것.
 * 입력에 사용할 함수의 입력 실패 조건을 반복 조건에 활용해야 함.
 * 
 * - 생각
 * 빈 줄과 공백이 문자에 포함되기 때문에 
 *  
 * SOLVE 1> 
 * fgets()는 개행을 입력 구분자로 하면서, 개행 입력 또한 지원하기
 * 때문에 이 경우에도 적용 가능
 *  
 * SOLVE 2>
 * getchar()를 이용해 한 글자씩 입력.
 * 
*/

// Solve 1
#include <stdio.h>
#define MAX_BUF 101

int main()
{
    char buf[MAX_BUF] = {0, };

    while(fgets(buf, MAX_BUF, stdin))
    {
        fprintf(stdout, "%s", buf);
    }

    return 0;
}