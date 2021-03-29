#include <iostream>
using namespace std;
#include <stdio.h>

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for(int i=1; i<=N; i++)
	{
		for(int j=1; j<=i; j++)
		{
			printf("*");
		}
		puts("");
	}
	
}