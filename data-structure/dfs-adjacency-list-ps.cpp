#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

const int MAX = 10;
vector<int> a[10];
int check[MAX];

void dfs(int x);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie();

    // n : vertex count, m :edge count
    int n, m; cin >> n >> m;

    //inplement the graph using adjacency list
    for(int i=0; i<m; i++){
        // u : vertex1, v : vertex2
        int u, v; cin >> u >> v;

        //store the vertex input data to the vector which is parts of graph
        a[u].push_back(v);
        a[v].push_back(u);
    }

    //use implemented graph
    for(int i=1; i<=n; i++){
        // i : vertex1
        cout << i << " : ";
        for(int j=0; j<a[i].size(); j++){
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }

    // dfs in adjacency list graph implementation
    dfs(3); cout << endl;
    memset(check, 0, 10*sizeof(int));
    dfs(1); cout << endl;
}

// x : vertex to visit
void dfs(int x)
{
    cout << x << ' ';
    check[x] = true;

    for(int i=0; i<a[x].size(); i++){
        if(check[a[x][i]] == false){
            dfs(a[x][i]);
        }
    }

}
