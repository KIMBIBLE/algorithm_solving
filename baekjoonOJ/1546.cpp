#include <iostream>
using namespace std;
#include <vector>

void input(vector<int> &in, int cnt);
void testPrint(vector<int> &in, int cnt);
int getMax(vector<int> &in, int cnt);
double solve(vector<int> &in, int max, int cnt);

int main()
{
	int N;
	cin >> N;
	
	vector<int> in;
	input(in, N);
	
	int max = getMax(in, N);
	double res = solve(in, max, N);

	cout << fixed;
	cout.precision(2);
	cout << res << endl;
	
}

double solve(vector<int> &in, int max, int cnt)
{
	double sum = 0;
	for(int i=0; i<cnt; i++)
	{
		sum += in[i];
	}
	
	return sum / cnt / max * 100;
}
	
void input(vector<int> &in, int cnt)
{
	int tmp;
	
	for(int i=0; i<cnt; i++)
	{
		cin >> tmp;
		in.push_back(tmp);
	}
}

void testPrint(vector<int> &in, int cnt)
{
	cout << "start test!" << endl;
	for(int i=0; i<cnt; i++)
	{
		cout << in[i] << " ";
	}
	cout << endl;
}

int getMax(vector<int> &in, int cnt)
{
	int max;
	max = in[0];
	for(int i=1; i<cnt; i++)
	{
		if(max < in[i])
			max = in[i];
	}
	return max;
}