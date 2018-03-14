/* 
 * # 10816 : 숫자 카드 2
 * - 문제
 * 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
 * 상근이는 숫자 카드 N개를 가지고 있다. 숫자 M개가 주어졌을 때, 
 * 이 숫자가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 
 * 구하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N 
 * (1 ≤ N ≤ 500,000)이가 주어진다. 둘째 줄에는 숫자 카드에 
 * 적혀있는 숫자가 주어진다. 숫자 카드에 적혀있는 숫자는 
 * -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
 * 셋째 줄에는 M (1 ≤ M ≤ 500,000)이 주어진다. 
 * 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할
 * M개의 숫자가 주어지며, 이 숫자는 공백으로 구분되어져 있다. 
 * 이숫자도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
 * 
 * - 출력
 * 첫째 줄에 입력으로 주어진 M개의 숫자에 대해서, 각 숫자가 
 * 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 
 * 구분해 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 숫자 카드 문제와 형태는 비슷하나, 중복 입력이 들어올 수 있다는
 * 점에서 차이가 생길 수 있다. 중복을 허용하지 않는 set 자료구조
 * 같은 경우는 사용이 불가능하기 때문에 다른 자료구조를 선택해야
 * 한다. 헤당 문제는 N개의 데이터에서 M개의 데이터가 존재하는지 
 * 검사하는 문제이기 때문에 (N개의 데이터에서 선택)*M 이라는
 * 알고리즘을 따를 것이고, 결국 N개의 데이터에서 선택하는
 * 부분에 대한 성능이 전체 성능에 가장 큰 영향을 미칠것이다.
 * vector나 array로 구현할 경우 M개 데이터에 대한 탐색 시간이
 * linear한 시간이 소요될 것이고, 
 * list를 사용할 경우, n^2(M*N)의 시간이 소요 될 것이다.
 * 이 경우 multiset을 사용하면 1회 탐색에 logN의 시간이 소요되기
 * 때문에 총 M*logN의 시간이 소요되기 때문에 성능적인 장점이 있다.
 * 
 * 
 * - 생각
 * 
 * 
 * SOLVE 1> 
 * multiset에 데이터를 저장하고, count를 출력하는 방식에서
 * timeout이 발생한다. multiset을 사용한는 것 보다
 * 효율적인 방식을 고민해야 할 듯.
 * O(NlogN)보다 빠른 방법을 찾아야 함.
 * 
 * 출력 포맷 정리
 * %d    -   int
 * %u    -   unsigned
 * %ld   -   long
 * %lld  -   long long
 * %lu   -   unsigned long
 * %llu  -   unsigned long long
*/

// Solve 1
#include <set>
#include <iostream>
using namespace std;

int main()
{
    int N, M;
    multiset<int> m;
    int num;

    scanf("%d", &N);
    for(int i=0; i<N; i++)
    {
        scanf("%d", &num);
        m.insert(num);
    }

    scanf("%d", &M);
    for(int i=0; i<M; i++)
    {
        scanf("%d", &num);
        printf("%lu ", m.count(num));
    }

}