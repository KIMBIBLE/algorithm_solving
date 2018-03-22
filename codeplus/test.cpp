#include <iostream>
#include <list>
using namespace std;
int main() {
    int n;
    list<pair<int,int>> a;
    cin >> n;

    for (int i=1; i<=n; i++) {
        int x;
        cin >> x;
        a.push_back({x,i});
    }

    auto it = a.begin();
    while(a.size()-1) {
        cout << (it->second) << ' ';
        int step = it->first;
        if (step > 0) {
            auto temp = it;
            ++temp;
            if (temp == a.end()) {
                temp = a.begin();
            }
            a.erase(it);
            it = temp;
            for (int i=1; i<step; i++) {
                ++it;
                if (it == a.end()) {
                    it = a.begin();
                }
            }
        } else if (step < 0) {
            step = -step;
            auto temp = it;
            if (temp == a.begin()) {
                temp = a.end();
            }
            --temp;
            a.erase(it);
            it = temp;
            for (int i=1; i<step; i++) {
                if (it == a.begin()) {
                    it = a.end();
                }
                --it;
            }
        }
    }

    cout << a.front().second << '\n';

    return 0;
}