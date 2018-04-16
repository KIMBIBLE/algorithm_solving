/*
아래의 케이스에 주의!
input>
3
2 1 2

output>
2

sum을 나누는 방식으로 구현할 경우, 나눴을 때 버려지는 1값이
결과에 영향을 미칠수가 있음. 이를 고려하여 코딩하기 위한 방법은
여러가지가 있지만, 간단히 sum을 나누지 않고 더하는 값만 2배 곱하여
구하면 간단하게 구할 수 있음.
*/

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