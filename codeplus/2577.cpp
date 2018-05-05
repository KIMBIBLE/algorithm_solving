#include <iostream>
using namespace std;

int cnt[10];

int main()
{
    long long a, b, c; cin >> a >> b >> c;
    long long res = a * b * c;
    while(res != 0){
        cnt[res % 10]++;
        res /= 10;
    }
    for(int i=0; i<10; i++){
        cout << cnt[i] << '\n';
    }
}
