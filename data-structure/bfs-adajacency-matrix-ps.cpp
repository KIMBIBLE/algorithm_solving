#include <iostream>
#include <queue>
using namespace std;

const int MAX = 10;
int a[MAX][MAX];
queue<int> q;
int check[MAX];

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int n, m; cin >> n >> m;

    for(int i=0; i<m; i++){
        int u, v, w; cin >> u >> v >> w;
        a[u][v] = a[v][u] = w;
    }

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }

    int start = 1;
    q.push(start); check[start] = true;

    while(!q.empty()){
        int data = q.front(); q.pop();
        cout << data;

        for(int i=1; i<=n; i++){
            if(check[i] == false && a[data][i] >=1){
                check[i] = true;
                q.push(i);
            }
        }
    }
    cout << endl;

}
