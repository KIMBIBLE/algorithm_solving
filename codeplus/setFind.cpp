#include <set>
#include <iostream>
using namespace std;

void print(set<int> &s, set<int>::iterator it);
int main()
{
    set<int> s = {7, 5, 3, 1};
    auto it = s.find(1);
    print(s, it);   //1
    
    it = s.find(2);
    print(s, it);   //end

    it = s.find(3);
    print(s, it);   //3
    
    it = s.find(4);
    print(s, it);   //end


}

void print(set<int> &s, set<int>::iterator it)
{
    if(it == s.end())
    {
        cout << "end" << endl;
    }
    else
    {
        cout << *it << endl;
    }
}