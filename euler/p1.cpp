/*
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

n보다 작은 수 중 공배수를 제외한 각각 3의 배수와 5의 배수 + 3, 5의 공배수

*/
#include <bits/stdc++.h>
using namespace std;

int gcd(int x, int y);
int lcm(int x, int y);

int main()
{
    ios_base::sync_with_stdio(false), cin.tie( NULL );
    int n=1000, x=3, y=5;
    vector <bool> v(n, false);

    int l = lcm(x, y);
    int sum=0;
    for(int i=0; i<n; i+=3){
        v[i] = true;
    }
    for(int i=0; i<n; i+=5){
        v[i] = true;
    }
    for(int i=0; i<n; i+=l){
        v[i] = true;
    }
    for(int i=0; i<n; i++){
        if(v[i]) sum += i;
    }
    cout << sum;
}

int gcd(int x, int y){
    if(x<y) swap(x, y);
    if(y==0) return x;

    gcd(y, x%y);
}

int lcm(int x, int y){
    return x * y / gcd(x, y);
}