#include <iostream>
using namespace std;

typedef long long ll;

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    ll a, b, c; cin >> a >> b >> c;

    ll res = 1;
    while(b--){
        res *= a;
        res %= c;
    }
    cout << res << endl;
}
