#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int main()
{
    list <int> l;
    cout << "l.size() : " << l.size() << endl; // size = 0
    l.push_back(1);
    cout << "l.size() : " << l.size() << endl; // size = 1
    l.push_back(2);
    l.push_back(3);
    
    auto p = [&](){
        cout << endl << "list element : ";

        for(auto each : l){
            cout << each << ' ';
        }
        cout << endl;
    };

    auto e = [&](auto it){
        cout << "erase element : " << *it << endl;
        it =  l.erase(it);
        cout << "l.size() : " << l.size() << endl;
        if(l.begin() == l.end())
            cout << "list is empty!" << endl;

        return it;
    };

    p(); // 1 2 3

    auto iter = l.begin();
    cout << "l.begin() : " << *iter << endl;
    cout << "l.end() : " << *l.end() << endl; // 1 3
    // end : past the end of sequence 이기 때문에
    // 3 다음의 위치를 가리키는 상태라 3이 출력이 안될 줄
    // 알았는데 출력이 됨.

    cout << "l.rend() : " << *l.rend() << endl;
    cout << "l.rbegin() : " << *l.rbegin() << endl;
    cout << "l.size() : " << l.size() << endl;


    p();
    cout << "l.begin() : " << *l.begin() << endl;
    cout << "l.end() : " << *l.end() << endl;

    iter = e(iter); // erase '1'
    p();
    cout << "l.begin() : " << *l.begin() << endl;
    cout << "l.end() : " << *l.end() << endl;

    iter = e(iter); // erase '2'
    p();
    cout << "l.begin() : " << *l.begin() << endl;
    cout << "l.end() : " << *l.end() << endl;

    iter = e(iter); // erase '3'
    cout << "l.begin() : " << *l.begin() << endl;
    cout << "l.end() : " << *l.end() << endl;

    // cout << l.size() << endl; // 이렇게 iteraor가 이전 노드를 가리키는 경우
    // double free같은게 발생할 수도 있겠구나!!!
    p();

    list <int> l2;
    l2.push_back(1);
    l2.push_back(2);
    l2.push_back(3);

    auto it = l2.begin();
    cout << endl << *it << endl;
    ++it;
    cout << *it << endl;
}