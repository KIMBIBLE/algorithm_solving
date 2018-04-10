#include <iostream>
#include <vector>
using namespace std;

char cmpRet(int &a, int &b);

int res = 0;

int main()
{
    int n, a, b;
    cin >> n >> a >> b;
    vector<char> x(n);
    for(int i=0; i<n; i++){
        cin >> x[i];
    }
    
    char prev = '.';
    char now;
    for(int i=0; i<n; i++){
        if(a == 0 && b == 0) break;
        if(x[i] == '.'){
            if(prev == 'a' && b > 0){
                res++;
                b--;
                prev = x[i];
            }
            else if(prev == 'b' && a > 0){
                res++;
                a--;
                prev = x[i];
            }
            else{
                prev = cmpRet(a, b);
            }
        }

        
    }    
    cout << res;
}


char cmpRet(int &a, int &b){
    if(a>b && a != 0){
        a--;
        return 'a';
    }
    else if(a<b && b != 0){
        b--;
        return 'b';
    }
    return '*';
}