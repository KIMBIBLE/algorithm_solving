/* 
 * # 11816 : 8진수, 10진수, 16진수
 * - 문제
 * 정수 X가 주어진다. 정수 X는 항상 8진수, 10진수, 16진수 중에 하나이다.
 * 8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.
 * X를 10진수로 바꿔서 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 X가 주어진다. X는 10진수로 바꿨을 때, 1,000,000보다 작거나 같은 자연수이다.
 * 16진수인 경우 알파벳은 소문자로만 이루어져 있다.
 * 
 * - 출력
 * 첫째 줄에 입력받은 X를 10진수로 바꿔서 출력한다.
 * 
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 입력으로 8진수, 10진수, 16진수 중 1개의 정수가 주어진다.
 * 10진수와 달리 8진수와 16진수의 경우 각각 0, 0x 형태의 prefix가 붙기 때문에
 * 입력으로 주어진 값이 몇 진수의 형태를 갖는지 구분해 주어야 한다.
 * 
 * - 생각
 * 입력값의 진수 형태를 구분해주기 위한 방법으로 아래의 두 가지 방법을 생각해 볼 수 있다.
 * 
 * SOLVE 1> 입력값을 문자열 형태로 받은 후, 진수의 형태에 따라 sscanf의 형식 지정자를 지정해 줌.
 * (10진수 : %d. 8진수 : %o, 16진수 : %x)
 * 
 * 이 방법에서 중요한 것은 문자열 형태로 저장한 입력값을 어떤 기준에 따라 
 * 분류할지를 결정하는 것이다.
 * 분류 기준을 정하기 위해 일단 8,10,16진수일 때의 입력값의 형태를 살펴보자.
 * 13(10) == 015(8) == 0xc(16) //문제 조건에 16진수의 경우 소문자 알파벳으로만 구성된다고 명시.
 * 위의 형태를 볼 때 아래와 같은 구분 기준을 정할 수 있다.
 * 10진수 <-> 8, 16 진수를 구분하는 기준은 문자열의 시작이 '0'인지
 * 8 <-> 16 진수를 구분하는 기준은 다음 문자가 소문자 'x'인지
 * 
 * 마지막으로 입력값의 최대 값이 1,000,000(10)이기 때문에 int 자료형을 사용하면 된다.
 * 
 * 
 * SOLVE 2> scanf의 %i 형식 지정자를 이용
*/

// Solve 2
#include <stdio.h>

int main()
{
    int num;
    scanf("%i", &num);
    printf("%d", num);
}
