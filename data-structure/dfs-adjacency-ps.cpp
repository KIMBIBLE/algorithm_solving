#include <iostream>
using namespace std;

const int MAX = 10;

int a[MAX][MAX];
int check[MAX];

void dfs(int x, int n);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int n, m; cin >> n >> m;
    for(int i=0; i<m; i++){
        int u, v; cin >> u >> v;
        a[u][v] = a[v][u] = 1;
    }

    dfs(1, n);
    cout << endl;

}

void dfs(int x, int n)
{
    check[x] = true;
    cout << x << ' ';
    for(int i=1; i<=n; i++){
        if(a[x][i] == 1 && check[i] == false){
            dfs(i, n);
        }
    }
}
