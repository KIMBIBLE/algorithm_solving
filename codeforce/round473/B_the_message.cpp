#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, m;
    cin >> n >> k >> m;
    vector<pair<string, int>> v(n+1);

    for(int i=1; i<=n; i++){
        cin >> v[i].first;
    }

    for(int i=1; i<=n; i++){
        cin >> v[i].second;
    }

    for(int i=1; i<=k; i++){
        int cnt;
        cin >> cnt;
        if(cnt == 1){
            cin >> cnt; // meaningless input
        }
        else{
            vector<int> tmp(cnt);

            for(int j=0; j<cnt; j++){
                cin >> tmp[j];
            }
            
            int min = v[tmp[0]].second;
            for(int j=0; j<cnt; j++){
                if(min > v[tmp[j]].second) min = v[tmp[j]].second;
            }

            for(int j=0; j<cnt; j++){
                v[tmp[j]].second = min;
            }
        }
    }

    int sum = 0;
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