#include <iostream>
using namespace std;

#define MAX_PLACE_VALUE 10

bool isHanNumber(int num);
int getPlaceValueAry(int *ary, int num);

int main()
{
    int num;
    cin >> num;
    int cnt = 0;
    for(int i=1; i<=num; i++)
    {
        if(isHanNumber(i))
            cnt++;
    }
    cout << cnt;
}

int getPlaceValue(int *ary, int num)
{
    int idx = 0;

    while(num)
    {
        ary[idx++] = num % 10;
        num /= 10;
    }

    return idx;
}

bool isHanNumber(int num)
{
    int sub_value;
    if(num < 100)
        return true;

    int numAry[10];
    int placeValueLen=getPlaceValue(numAry, num) - 1;
    int subValue = numAry[0] - numAry[1];
    for(int i=1; i<placeValueLen; i++)
    {
        if(numAry[i] - numAry[i+1] != subValue)
            return false;
    }
    return true;
}


