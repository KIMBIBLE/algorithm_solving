/*
 * < Priority Queue > : (default)최대 힙
 * 가장 큰 요소에 접근하는데 걸리는 시간이 상수 시간이 걸림.
 * 삽입, 삭제에 대한 비용은 logN
 * 
 * std::greater<T>를 사용하면 Priority Queue를 최소 힙으로
 * 사용할 수 있다.
 * 
 * # parameter usage
 * template<
 *    class T,
 *    class Container = std::vector<T>,
 *    class Compare = std::less<typename Container::value_type>
 * > class priority_queue;
 * 
 * - class T : 해당 컨테이너에 저장할 데이터의 자료형
 * 
 * - class Container : priority queue를 구성하는 자료형
 *   연관 컨테이너만 사용 가능하며, RandomAccessIterator를
 *   지원하는 컨테이너여야 한다. 해당 컨테이너에
 *   front(), push_back(), pop_back()의 함수 포함되어야한다.
 *   => 위의 조건 3개를 모두 만족하는 컨테이너에는
 *   vector, deque가 있다.
 * 
 * - class Compare : 비교 타입은 strict weak ordering 방식을
 *   사용한다. 기본 지정값은 less<typename Container::value_type>이다.
 * 
 * 
 * reference : 
 * http://en.cppreference.com/w/cpp/container/priority_queue
 * 
 */

#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

template<typename T> void print_queue(T& q) {
    while(!q.empty()){
        cout << q.top() << " ";
        q.pop();
    }
    cout << '\n';
}

int main()
{
    priority_queue<int> q1;

    for(int n: {1,8,5,6,3,4,0,9,7,2})
        q1.push(n);

    print_queue(q1);
    // 8 7 6 5 4 3 2 1 0

    priority_queue<int, vector<int>, greater<int> > q2;
    for(int n : {1,8,5,6,3,4,0,9,7,2})
        q2.push(n);

    print_queue(q2);
    // 0 1 2 3 4 5 6 7 8 9

    //using lambda to compare elements.
    auto cmp = [](int left, int right) { return (left ^ 1) < (right ^ 1);};
    priority_queue<int, vector<int>, decltype(cmp)> q3(cmp);

    for(int n: {1,8,5,6,3,4,0,9,7,2})
        q3.push(n);

    print_queue(q3);
    // 8 9 6 7 4 5 2 3 0 1

    vector<int> a = {3, 5, 1, 2, 4};
    priority_queue<int, vector<int>, greater<int>> q4; //최소 힙
    for(int x : a)
        q4.push(x);
    print_queue(q4);
    // 1 2 3 4 5
}