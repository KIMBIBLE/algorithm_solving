#include <iostream>
#include <string>
using namespace std;

#define MAX_LINE 100

int main(int argc, char* argv[])
{
	string line;
	while(1)
	{
		getline(cin, line);
		if(line == "")
			break;
		cout << line << endl;
	}
	
}