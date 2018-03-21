#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s = "asdf";
    printf("%s\n", s.c_str());

    printf("%d\n", s.size());
    printf("%d\n", s.length());

    s = "";
    printf("%d\n", s.size());

    s = "asdfqwer";
    s[5] = 0;
    printf("%s\n", s.c_str());
    cout << s << '\n';

    printf("%d\n", s.size());
    printf("%d\n", s.length());
}