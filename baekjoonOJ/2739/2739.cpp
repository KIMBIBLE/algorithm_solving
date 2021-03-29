#include <iostream>
using namespace std;
#include <stdio.h>

int main(int argc, char *argv[])
{
	int N;
	cin >> N;
	
	for(int i=1; i<=9; i++)
	{
		printf("%d * %d = %d\n", N, i , N*i);
	}
}