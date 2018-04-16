/* Write up
문제 분석>
A -> B로 특정 언어의 메시지를 보낸다.
이 언어에는 총 n개의 단어가 존재.
각 단어는 독립적인 것이 아니라 다른 언어와 의미가 겹치는 것이 존재.
n개의 단어에서 같은 의미를 가지는 단어를 k개의 그룹으로 묶었을 때,
모든 단어는 한가지 그룹에 속해있게 된다.

단어들로 구성된 메시지가 주어지고 메시지에 포함된 각각의 단어의 비용이
주어졌을 때, 의미가 겹치는 단어를 비용이 싼 단어로 교체하여
최소의 비용으로 메시지를 보내는 문제.
(1<=k<=n<=10^5, 1<=m<=10^5), 비용:a1,a2,,,,an(1<=ai<=10^9)

입출력>
#input1
5 4 4
i loser am the second
100 1 1 5 10
1 1
1 3
2 2 5
1 4
i am the second

#output1
107

#input2
5 4 4
i loser am the second
100 20 1 5 10
1 1
1 3
2 2 5
1 4
i am the second

#output2
116

*/

#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
const size_t N = 1000000;

int main()
{
    int n, k, m;
    ios_base::sync_with_stdio( false ), cin.tie( nullptr );
    cin >> n >> k >> m;

    string s; 
    unordered_map<string, int>um;
    for(int i=0; i<n; i++){
        cin >> s; 
        um[s] = i;
    }

    int cost[N];
    for(int i=0; i<n; i++)
        cin >> cost[i];
    
    for(int i=0; i<k; i++){
        int cnt; cin >> cnt;
        if(cnt == 1){ 
            cin >> cnt; 
            continue; // meaningless input
        }

        int indices[N];
        ull min_num = -1; // set min to max value

        // get min
        for(int j=0; j<cnt; j++){
            cin >> indices[j]; --indices[j];
            if(min_num > cost[indices[j]]) min_num = cost[indices[j]];
        }

        // set cost to min
        for(int j=0; j<cnt; j++)
            cost[indices[j]] = min_num;
    }

    ull sum = 0;
    for(int i=0; i<m; i++){
        cin >> s;
        sum += cost[um[s]];
    }
    cout << sum;
}








/* First solution => Fail(time limit)

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, m;
    ios_base::sync_with_stdio( false ), cin.tie( nullptr );
    cin >> n >> k >> m;
    vector<pair<string, unsigned long long>> v(n+1);

    for(int i=1; i<=n; i++){
        cin >> v[i].first;
    }

    for(int i=1; i<=n; i++){
        cin >> v[i].second;
    }

    for(int i=1; i<=k; i++){
        int cnt;
        cin >> cnt;
        unsigned long long min = -1; // max value
        if(cnt == 1){
            cin >> cnt; // meaningless input
        }
        else{
            vector<int> tmp(cnt);
            v[0].second = -1;
            for(int j=0; j<cnt; j++){
                cin >> tmp[j];
                if(min > v[tmp[j]].second) min = v[tmp[j]].second;
            }
            
            for(int j=0; j<cnt; j++){
                v[tmp[j]].second = min;
            }
        }
    }

    unsigned long long sum = 0;
    string tmp;
    for(int i=0; i<m; i++){
        cin >> tmp;
        for(int j=1; j<=n; j++){
            if(v[j].first == tmp){
                sum += v[j].second;
            }
        }
    }
    
    cout << sum;
}
*/

/* 다른사람이 푼거
#include <bits/stdc++.h>

using namespace std;

const size_t N = 100000;

int group[ N ], cost[ N ], min_cost[ N ]; long long solution;

int main()
{
    int k, m, n, u, x; string s; unordered_map< string, int > word_index;

    ios_base::sync_with_stdio( false ), cin.tie( nullptr ), cin >> n >> k >> m;

    for( int i = 0; i < n; i++ )
        cin >> s, word_index[ s ] = i;

    for( int i = 0; i < n; i++ )
        cin >> cost[ i ];

    for( int i = 0; i < k; min_cost[ i++ ] = u )
    {
        u = INT_MAX, cin >> x;

        for( int j = 0; j < x; j++ )
        {
            int c, l; cin >> l, c = cost[ --l ], group[ l ] = i;

            if ( c < u )
                u = c;
        }
    }

    for( int i = 0; i < m; i++ )
        cin >> s, solution += min_cost[ group[ word_index[ s ] ] ];

    cout << solution;
}

*/