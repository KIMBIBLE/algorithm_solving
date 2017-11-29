#include <iostream>
using namespace std;

int main()
{
	int N, start;
	int value;
	int cnt = 0;
	cin >> N;
	start = N;
	
	while(1)
	{
		cnt++;
		value = (N/10 + N%10)%10;
		value = N%10*10 + value;
		if(start == value)
			break;
		N = value;
	}
	cout << cnt;
}