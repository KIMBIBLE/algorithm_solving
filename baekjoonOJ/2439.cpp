#include <iostream>
using namespace std;
#include <stdio.h>

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	
	for(int i=5; i>=1; i--)
	{
		for(int j=1; j<=5; j++)
		{
			if(i <= j)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
}