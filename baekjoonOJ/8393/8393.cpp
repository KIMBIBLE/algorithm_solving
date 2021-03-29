#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	int n;
	cin >> n;
	
	int sum = 0;
	while(n)
	{
		sum += n--;
	}
	
	cout << sum;
}