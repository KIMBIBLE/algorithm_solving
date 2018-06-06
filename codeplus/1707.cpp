/* # 1707 : 이분 그래프
- 문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

- 입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가
빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

- 출력

- 시간 제한 : 2초

# writeup
- 분석
bipartiate graph를 판별하는 문제. 그래프의 component가 2개인지를 판별하면 된다.

- 생각


SOLVE1>
1. cnt : 테스트 케이스 수 만큼 반복 - LOOP(cnt)
각 테스트 수행 시 마다 check, adjacency list, component 초기화 필요

2. 그래프 초기화 (adjacency list)

3. 각 vertex(1<=v<=n)를 dfs 를 통해 방문하고 component 갯수 누적

4. component 갯수 == 2 일 때 bipartiate graph
*/ // SOLVE1
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAX = 20001;
int check[MAX];
vector<int> a[MAX];
int component;

void solve();
void dfs(int node);
void probClear();

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int k; cin >> k;
    while(k--){
        solve();
    }
}

void solve(){
    int n, m; cin >> n >> m;
    for(int i=0; i<m; i++){
        int u, v; cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }

    for(int i=1; i<=n; i++){
        if(check[i] == false && a[i].size() != 0){
            component++;
            dfs(i);
        }
    }

    if(component == 2) cout << "YES" << endl;
    else cout << "NO" << endl;

    probClear();
}

void dfs(int node){
    check[node] = component;

    for(int i=0; i<=a[node].size(); i++){
        int next = a[node][i];
        if(check[next] == false){
            dfs(next);
        }
    }
}



void probClear(){
    memset(check, 0, sizeof(check));
    for(int i=1; i<=MAX; i++){
        a[i].clear();
    }
    component = 0;
}
