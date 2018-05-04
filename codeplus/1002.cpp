
#include <iostream>

using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    int t; cin >> t;

    while(t--) {
       ll x1, y1, r1, x2, y2, r2;
       cin >> x1 >> y1 >> r1 >>x2 >>y2 >> r2;
       ll dx = x1-x2;
       ll dy = y1-y2;
       ll d = dx*dx + dy*dy;

       ll add = r1 + r2;
       ll sub = r1 - r2;
       add *= add;
       sub *= sub;

       if (sub < d && d < add) {
           cout << 2;
       } else if (d == add || (d == sub && d != 0) ) {
           cout << 1;
       } else if (d < sub || add < d) {
           cout << 0;
       } else if (d == 0) {
           if (r1 == r2)
               cout << -1;
           else
               cout << 0;
       }
       cout << '\n';
    }
    return 0;

}
