#include <iostream>
#include <vector>
#include <algorithm>
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
    if(n == 1){
        return 0;
    }
    if(d[n] > 0) return d[n];

    d[n] = solve(d, n-1) + 1;

    if(n%3 == 0){
        int tmp = solve(d, n/3) + 1;
        if(d[n] > tmp)
            d[n] = tmp;
    }
    if(n%2 == 0){
        int tmp = solve(d, n/2) + 1;
        if(d[n] > tmp)
            d[n] = tmp;
    }
    
    

    return d[n];
}
