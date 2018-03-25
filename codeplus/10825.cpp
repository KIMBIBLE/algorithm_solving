/* 
 * # 10825 : 국영수
 * - 문제
 * 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 
 * 이 때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
 * 
 * 국어 점수가 감소하는 순서로
 * 국어 점수가 같으면 영어 점수가 증가하는 순서로
 * 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
 * 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 
 * (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
 * 
 * - 입력
 * 첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 
 * 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 
 * 공백으로 구분해 주어진다. 점수는 1보다 크거나 같고, 100보다 작거나 
 * 같은 자연수이다. 이름은 알파벳 대소문자로 이루어진 문자열이고, 
 * 길이는 10자리를 넘지 않는다.
 * 
 * - 출력
 * 문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.
 *  
 * *********************************************************************************
 * 
 * # writeup
 * - 분석
 * 
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
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Person{
    string name;
    int kor, eng, math;
};

bool cmp(const Person &u, const Person &v);

int main()
{
    int n;
    cin >> n;
    vector<Person> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i].name >> a[i].kor >> a[i].eng >> a[i].math;
    }

    sort(a.begin(), a.end(), cmp);

    for(int i=0; i<n; i++){
        cout << a[i].name << '\n';
    }
}

bool cmp(const Person &u, const Person &v)
{
    if(u.kor ==  v.kor){
        if(u.eng == v.eng){
            if(u.math == v.math){
                return u.name < v.name;        
            }
            return  u.math > v.math;
        }
        return u.eng < v.eng;
    }
    else{
        return u.kor > v.kor;
    }
}