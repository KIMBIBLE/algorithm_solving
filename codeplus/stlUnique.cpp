/*
 * STL Unique Usage
 * [begin, end)의 구간에서 연속되는 같은 값을 하나만
 * 남기고 나머지는 제거한다.
 * 
 * 컨테이너의 크기는 변경되지 않으며, 내부적으로
 * 중복을 덮어씌우거나 시프트시키는 방법으로 구현됨.
 *  
 * http://en.cppreference.com/w/cpp/algorithm/unique
 */
#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;

template<class ForwardIt>
ForwardIt unique1(ForwardIt first, ForwardIt last)
{
    //unique()는 중복을 제거한 후의 end iter를 리턴한다.
    if (first == last)  // 컨테이너가 비어있는 경우
        return last;

    // 연속된 중복값 제거
    // result : 현재 loop에서 제거할 중복값
    ForwardIt result = first;
    while (++first != last) {
        // result : 중복이 제거된 값의 위치
        if (!(*result == *first) && ++result != first) {
            *result = std::move(*first);
        }
    }
    return ++result;
}

template<class ForwardIt, class BinaryPredicate>
ForwardIt unique2(ForwardIt first, ForwardIt last, BinaryPredicate p)
{
    if (first == last)
        return last;
 
    ForwardIt result = first;
    while (++first != last) {
        if (!p(*result, *first) && ++result != first) {
            *result = std::move(*first);
        }
    }
    return ++result;
}

int main()
{
    cout << "unique usage 1" << '\n';
    vector<int> v = {1, 1, 2, 2, 2, 3, 1, 1, 1, 2, 2, 2, 2};

    function<void(vector<int> &)> print = [](vector<int> &r){
        for(int x : r){
            cout << x << ' ';
        }
        cout << '\n';
    };
    auto last = unique1(v.begin(), v.end());

    print(v);

    for(auto it = v.begin(); it != last; ++it){
        cout << *it << ' ';
    }
    cout << "\n\n";

    cout << "unique usage 2" << '\n';

    vector<int> v2 = {1, 1, 2, 2, 2, 3, 1, 1, 1, 2, 2, 2, 2};
    sort(v2.begin(), v2.end());
    auto last2 = unique1(v2.begin(), v2.end());
    v2.erase(last2, v2.end());
    print(v2);
    cout << "\n\n";

    cout << "unique usage 3" << '\n';

    // remove consecutive spaces
    string s = "wanna go    to      space?";
    auto end = unique2(s.begin(), s.end(), [](char l, char r){
        return isspace(l) && isspace(r) && l == r;
    });
    cout << s << '\n';
    cout << string(s.begin(), end) << '\n';
}