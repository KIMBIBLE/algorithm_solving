#include <iostream>
using namespace std;

const int N = 10;
int a[N+1][N+1];

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);

    // n : edge cnt
    int n, m; cin >> n;
    for(int i=0; i<n; i++){
        int u, v; cin >> u >> v;
        a[u][v] = a[v][u] = true;
    }

    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }

}
