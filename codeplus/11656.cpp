/* 
 * # 11656 : 접미사 배열
 * - 문제
 * 접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
 * baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, 
 * oon, on, n 으로 총 8가지가 있고, 이를 사전순으로 정렬하면, 
 * aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
 * 
 * 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 
 * 출력하는 프로그램을 작성하시오.
 * 
 * - 입력
 * 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 
 * 길이는 1,000보다 작거나 같다.
 * 
 * - 출력
 * 첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * begin을 1씩 증가시켜 vector에 넣어두고
 * 문자열 vector를 정렬(merge sort)하면
 * O(NlogN) 복잡도가 나오고, 문자열의 길이는 1000정도이기 때문에
 * 시간제한 1초 내에 문제 해결 가능할 것으로 예상.
 * 
 * - 생각
 * 
 * 
 * SOLVE 1> 
 * 
 * 
*/

// Solve 1
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    cin >> s;
    vector <string> v;
    for(auto it=s.begin(); it != s.end(); ++it){
        string tmp(it, s.end());
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());
    for(auto x : v){
        cout << x << '\n';
    }
}