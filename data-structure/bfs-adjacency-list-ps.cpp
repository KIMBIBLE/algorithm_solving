#include <iostream>
#include <queue>
using namespace std;

const int MAX = 10;
vector<pair<int, int>> a[MAX];
int check[MAX];
queue<int> q;

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int n, m; cin >> n >> m;

    for(int i=0; i<m; i++){
        int u, v, w; cin >> u >> v >> w;
        a[u].push_back(make_pair(v, w));
        a[v].push_back(make_pair(u, w));
    }

    for(int i=1; i<=n; i++){
        cout << i << " : ";
        for(int j=0; j<a[i].size(); j++){
            cout << a[i][j].first << '(' << a[i][j].second << ") ";
        }
        cout << endl;
    }

    int start=1;
    q.push(start); check[start]=true;

    while(!q.empty()){
        int data = q.front(); q.pop();
        cout << data << ' ';

        for(int i=0; i<a[data].size(); i++){
            int v = a[data][i].first;
            if(check[v] == false){
                check[v] = true;
                q.push(v);
            }
        }
    } cout << endl;


}
