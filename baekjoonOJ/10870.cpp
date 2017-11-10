#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int num;
	cin >> num;
	
	if(num == 0)
		cout << 0;
	else if(num == 1)
		cout << 1;
	else{
		int back2 = 0;
		int back1 = 1;
		int fibo_num;
		for(int i = 2; i <= num; i++){
			fibo_num = back2 + back1;
			back2 = back1;
			back1 = fibo_num;
		}
		cout << fibo_num;
	}
}