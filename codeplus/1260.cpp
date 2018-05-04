/*
 * # 1260 : dfs와 bfs
 * - 문제
 *
 *
 * - 입력
 *
 *
 * - 출력
 *
 *
 * *********************************************************************************
 *
 * # writeup
 * - 분석
 *
 *
 * - 생각
 *
 *
 * SOLVE 1>
 *
 * 가중치가 없는 양방향 그래프의 dfs, bfs 탐색
 * adjacency list 사용하여 그래프 구현
*/

// Solve 1
#include <iostream>
#include <queue>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 1001;
vector<int> a[MAX];
bool check[MAX];

void dfs(int x);
void bfs(int x);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int n, m, s; cin >> n >> m >> s;
    for(int i=0; i<m; i++){
        int u, v; cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }

    for(int i=1; i<=n; i++){
        sort(a[i].begin(), a[i].end());
    }

    dfs(s);
    cout << endl;
    bfs(s);

}

void dfs(int x)
{
    check[x] = true;
    cout << x << ' ';
    for(int i=0; i<a[x].size(); i++){
        int next = a[x][i];
        if(check[next] == false){
            dfs(next);
        }
    }
}

void bfs(int x)
{
    queue<int> q;
    memset(check, false, sizeof(check));

    check[x] = true;
    q.push(x);

    while(!q.empty()){
        int data = q.front(); q.pop();
        cout << data << ' ';

        for(int i=0; i<a[data].size(); i++){
            int y = a[data][i];
            if(check[y] == false){
                check[y] = true;
                q.push(y);
            }
        }
    }
    cout << endl;
}
