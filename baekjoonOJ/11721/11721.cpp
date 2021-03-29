#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	char ch;
	int n = 1;
	while(1)
	{
		ch = cin.get();
		if(ch == '\n')
			break;
		cout << ch;
		if(!(n++ % 10))
			cout << endl;
	}
}