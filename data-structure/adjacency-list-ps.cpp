#include <iostream>
#include <vector>
using namespace std;

const int MAX = 10;
vector<pair<int, int>> a[MAX];

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);

    // n: vertex cnt, m : edge cnt
    int n, m; cin >> n >> m;

    for(int i=0; i<m; i++){
        int u, v, w;
        cin >> u >> v >> w;
        a[u].push_back(make_pair(v, w));
        a[v].push_back(make_pair(u, w));
    }

    for(int i=0; i<n; i++){
        for(int j=0; j < a[i].size(); j++){
            cout << i << " -> " << a[i][j].first << " : " << a[i][j].second << endl;
        }
        cout << endl;
    }
}
