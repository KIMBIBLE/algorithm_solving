#include <iostream>
using namespace std;

int solve(int *input);

int main(int argc, char *argv[])
{
	int input[3];
	for(int i=0; i<3; i++)
	{
		cin >> input[i];
	}

	cout << input[solve(input)];
	
}

int solve(int *input)
{
	int res;
	
	if(input[0] > input[1] && input[0] > input[2])
	{
		if(input[1] > input[2])
			res = 1;
		else
			res = 2;
	}
	else if(input[1] > input[0] && input[1] > input[2])
	{
		if(input[0] > input[2])
			res = 0;
		else 
			res = 2;
	}
	else
	{
		if(input[0] > input[1])
			res = 0;
		else
			res = 1;
	}
	
	return res;
}
