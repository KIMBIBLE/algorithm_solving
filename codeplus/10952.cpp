#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int a, b;
    while(1){
        cin >> a >> b;
        if(a == 0 && b == 0){break;}
        cout << a + b << '\n';
    }
}