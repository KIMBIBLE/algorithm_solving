#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> &, int);

int main()
{
    int n;
    cin >> n;
    vector<int> d(n+1, 0);

    cout << solve(d, n);
    
}

int solve(vector<int> &d, int n)
{
    if(n<=1) return n;
    if(d[n] >0 ) return d[n];

    d[n] = solve(d, n-2) + solve(d, n-1);

    return d[n];
}