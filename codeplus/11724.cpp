/* # 11724 : 연결 요소의 개수
- 문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

- 입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

- 출력
첫째 줄에 연결 요소의 개수를 출력한다.

- 시간제한 : 3초

# writeup
- 분석
1 <= N <= 1000
0 <= M <= nC2
그래프 종류는 상관이 없을 듯. 간선의 갯수가 최대 모든 vertex가 연결된 상태가 되기 때문에
edge list를 사용할 필요는 없을 듯.

- 생각
그래프는 adjacency list 사용. 연결 요소의 갯수 파악은
그래프의 모든 vertex를 dfs/bfs를 통해 방문하여
dfs/bfs의 시작 vertex가 이전에 방문하지 않은 vertex인 경우 component의 갯수를
추가해 주는 방식으로 코딩하면 될 듯.


SOLVE1>
1. 그래프 초기화(adjacency list)
2. 모든 vertex(1 ~ n)를 방문한다.
만약 이전에 방문하지 않은 vertex라면 component count 증가

*/ // SOLVE1
#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1001;
bool check[MAX];
vector<int> a[MAX];

void dfs(int node);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int n,m; cin >> n >> m;

    for(int i=0; i<m; i++){
        int u, v; cin >> u >> v;
        a[u].push_back(v); a[v].push_back(u);
    }

    int component = 0;
    for(int i=1; i<=n; i++){
        if(check[i] == false){
            dfs(i);
            component++;
        }
    }
    cout << component << endl;
}

void dfs(int node){
    check[node] = true;
    for(int i=0; i<a[node].size(); i++){
        int next = a[node][i];
        if(check[next] == false){
            dfs(next);
        }
    }
}
