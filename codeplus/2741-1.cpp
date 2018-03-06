/* 
 * # 2741 : N 찍기
 * - 문제
 * 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 
 * 출력하는 프로그램을 작성하시오.(1 초)
 * 
 * - 입력
 * 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
 * 
 * - 출력
 * 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 반복 횟수가 최대 100,000번 반복되는데 비해 시간 제한이
 * 1초로 짧게 주어진다.
 * 
 * - 생각
 * 입력 방식에 따라 속도 차이가 발생할 수 있으므로
 * 알고리즘 성능 분석 코드를 구현해 성능 비교를 할 필요가 있다.
 * 
 * stage 1 : 벤치마킹 소스코드 구현
 * 성능 분석을 위해 cpu 클럭 수를 측정하는 방법을 이용
 * 
 * SOLVE 1> 
 * printf 이용
 * Measure Time : 1.953125 Sec.
 * 
 * SOLVE 2>
 * cout + '\n'이용
 * Measure Time : 2.515625 Sec.
 * 
 * SOLVE 3>
 * cout + endl 이용
 * Measure Time : 2.390625 Sec.
 * 
 * 
*/

// Solve 1
#include <stdio.h>
#include <time.h>

int main()
{
    int N;
    clock_t startClock, endClock;
    scanf("%d", &N);

    // measure start clock
    startClock = clock();

    for(int i=1; i<=N; i++)
    {
        printf("%d\n", i);
    }
    
    // measure end clock
    endClock = clock();
    printf("Measure Time : %Lf Sec.\n", (long double)(endClock - startClock) / CLOCKS_PER_SEC);
}