#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
	int N, X;
	cin >> N >> X;
	
	int now;
	for(int i=0; i<N; i++)
	{
		cin >> now;
		if(now < X)
			cout << now << " ";
	}
}