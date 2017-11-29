#include <iostream>
using namespace std;
#include <vector>

double input(vector<int> &score, int cnt);
double solve(vector<int> &socre, int cnt, double avg);

int main()
{
	int C, N;
	double avg, ratio;
	vector<int> score;
	
	cin >> C;
	
	// set output's type
	cout << fixed;
	cout.precision(3);
	
	while(C--)
	{
		cin >> N;
		avg = input(score, N);
		cout << solve(score, N, avg) << "%" << endl;
	}
	
}

double input(vector<int> &score, int cnt)
{
	int tmp;
	score.clear();
	double sum = 0.0;
	for(int i=0; i<cnt; i++)
	{
		cin >> tmp;
		sum += tmp;
		score.push_back(tmp);
	}
	return sum/cnt;	//return cnt
}

double solve(vector<int> &score, int cnt, double avg)
{
	double total = 0;
	
	for(int i=0; i<cnt; i++)
	{
		if(score[i] > avg)
			total++;
	}
	
	return total / cnt * 100;
}