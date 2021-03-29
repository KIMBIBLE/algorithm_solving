#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	cin.get(); // clear '\n' in steram
	int sum = 0;
	while(N--)
	{
		sum += cin.get() - '0';
	}
	cout << sum;
}