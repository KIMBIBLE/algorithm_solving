#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> x(n);
    int sum = 0;

    for(int i=0; i<n; i++){
        scanf("%d", &x[i]);
        sum += x[i];
    }

    int res = 0;
    
    for(int i=0; i<n; i++){
        res += x[i] * 2;
        if(sum <= res) {
            printf("%d", i+1);
            break;
        }
    }

}