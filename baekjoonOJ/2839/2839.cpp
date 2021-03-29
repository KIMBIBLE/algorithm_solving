#include <iostream>
using namespace std;
 
#define PKG_3 3
#define PKG_5 5

int Solve(int N);

int main(int argc, char *argv[])
{
	int N;	// 3<=N<=5000
	cin >> N;
	
	cout << Solve(N);	
}

int Solve(int N)
{
	/*	5X + 3Y = N의 조건식
		조건식을 만족하는 여러 i, j 값 중 i값이 높은(5킬로 그램 봉지가 많은)
		값을 찾는 문제. 따라서 조건식을 만족하는 i, j 여러 쌍 중 최적값의
		우선순위를 i가 높을 때에 두기 위해, i를 높은 값부터 줄여가며 순차적으로 비교.
	*/
	for(int i = N/PKG_5; i >= 0; i--)
	{
		for(int j = 0; j <= N; j++)	// 사실상 j <= N이 아니라 j <= N/PKG_3 까지만 비교됨.
		{
			if((i * PKG_5) + (j * PKG_3) == N)
				return i + j;
		}
	}
	return -1;
}
