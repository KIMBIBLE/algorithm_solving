#include <iostream>
using namespace std;

#define MAX_VALUE 10000

bool solve(int num);
int addPlaceValue(int num);

int main()
{
    int num;
    for(int i=1; i<MAX_VALUE; i++)
    {
        if(solve(i))
            cout << i << endl;
    }
}

int addPlaceValue(int num)
{
    int res = 0;
    while(1)
    {
        res += num%10;
        num /= 10;
        if(!num)
            break;
    }
    return res + num;
}

bool solve(int num)
{
   for(int i=1; i<=MAX_VALUE; i++)
   {
       if(addPlaceValue(i)+i == num)
           return false;
   }
   return true;
}


