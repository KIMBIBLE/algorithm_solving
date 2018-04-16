#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, m;
    cin >> n >> k >> m;
    vector<pair<string, unsigned long long>> v(n+1);

    for(int i=1; i<=n; i++){
        cin >> v[i].first;
    }

    for(int i=1; i<=n; i++){
        cin >> v[i].second;
    }

    for(int i=1; i<=k; i++){
        int cnt;
        cin >> cnt;
        unsigned long long min = -1; // max value
        if(cnt == 1){
            cin >> cnt; // meaningless input
        }
        else{
            vector<int> tmp(cnt);
            v[0].second = -1;
            for(int j=0; j<cnt; j++){
                cin >> tmp[j];
                if(min > v[tmp[j]].second) min = v[tmp[j]].second;
            }
            
            for(int j=0; j<cnt; j++){
                v[tmp[j]].second = min;
            }
        }
    }

    unsigned long long sum = 0;
    string tmp;
    for(int i=0; i<m; i++){
        cin >> tmp;
        for(int j=1; j<=n; j++){
            if(v[j].first == tmp){
                sum += v[j].second;
            }
        }
    }
    
    cout << sum;
}