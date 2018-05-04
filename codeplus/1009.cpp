#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int t; cin >> t;
    while(t--){
        int a, b; cin >> a >> b;
        int res = 1;
        for(int i=1; i<=b; i++){
            res *= a;
            res %= 10;
        }
        if(res == 0) res = 10;
        cout << res << '\n';
    }
}
