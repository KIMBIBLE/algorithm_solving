#include <iostream>
using namespace std;
int main(int argc, char* argv[])
{
	int score;
	cin >> score;
	
	if(score >= 90)
	{
		cout << 'A';
		return 0;
	}
	else if(score >= 80)
	{
		cout << 'B';
		return 0;
	}
	else if(score >= 70)
	{
		cout << 'C';
		return 0;
	}
	else if(score >= 60)
	{
		cout << 'D';
		return 0;
	}
	else
		cout << 'F';
}