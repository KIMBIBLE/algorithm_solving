#include <iostream>
using namespace std;

const int MAX = 20;

int e[MAX][2];
int cnt[MAX]; // index : vertex

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);

    // n : vertex cnt, m : edge cnt
    int n, m; cin >> n >> m;

    // get edge(vertex1, vertex2) data
    for(int i=0; i<m*2; i++){
        cin >> e[i][0] >> e[i][1];
    }

    // cnt[x] : x번 간선과 연결된 정점의 수
    for(int i=0; i<m*2; i++){
        cnt[e[i][0]] += 1;
    }

    cout << "edge count about each vertex" << endl;
    for(int i=1; i<=n; i++){
        cout << i << " : " << cnt[i] << endl;
    }
    cout << endl;

    // cnt 단계별 누적
    for(int i=1; i<=n; i++){
        cnt[i] = cnt[i-1] + cnt[i];
    }

    // i번 정점과 연결된 간선은 e배열에서 cnt[i-1] ~ cnt[i] -1 까지
    for(int i=1; i<=n; i++){
        cout << i << " : " << cnt[i] - cnt[i-1] << endl;
    }
    cout << endl;

    for(int i=1; i<=n; i++){
        cout << i << " : ";
        for(int j=cnt[i-1]; j<cnt[i]; j++){
            cout << e[j][1] << ' ';
        }
        cout << endl;
    }
}
