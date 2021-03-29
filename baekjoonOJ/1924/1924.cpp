#include <iostream>
using namespace std;
#include <string>

int main()
{
	int X, Y;
	cin >> X >> Y;
	int total_day = 0;
	
	string day_list[7] = {
		"SUN",
		"MON",
		"TUE",
		"WED",
		"THU",
		"FRI",
		"SAT",
	};
	
	int month_value[13] = {
		0, // garbage value
		/* january ~ december's day */
		31, 28, 31, 30, 31,
		30, 31, 31, 30, 31,
		30, 31
	};
	
	for(int i = 0; i < X; i++)
	{
		total_day += month_value[i];
	}
	total_day += Y;
	
	cout << day_list[total_day % 7];
	
}