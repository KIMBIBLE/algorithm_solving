#include <iostream>
using namespace std;
#include <stdio.h>

int main (int argc, char *argv[])
{
	int N;
	cin >> N;
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<i; j++)
		{
			printf(" ");
		}
		for(int j=N; j>i; j--)
		{
			printf("*");
		}
		puts("");
	}
}