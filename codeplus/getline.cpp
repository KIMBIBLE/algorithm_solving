/* [C++11] getline()
 * std::getline(string)
 * - get line from stream into string
 * 
 * (1)	
 * - istream& getline (istream&  is, string& str, char delim);
 * - istream& getline (istream&& is, string& str, char delim);
 * (2)	
 * - istream& getline (istream&  is, string& str);
 * - istream& getline (istream&& is, string& str);
 * 
 * Extracts characters from is and stores them into str 
 * until the delimitation character delim is found 
 * (or the newline character, '\n', for (2)).
 * => is(istream)으로부터 문자를 받아 와 string 변수에 저장.
 * delim(구분자)를 만나면 입력 종료.
 * '(2)'의 경우 기본적으로 개행이 delim이 된다.
 * 
 * The extraction also stops if the end of file is reached 
 * in is or if some other error occurs during 
 * the input operation.
 * => delim으로 설정 된 입력 종료 조건 이외에도 
 * input operation의 에러나 istream에서 EOF를 읽어 올 경우
 * 입력을 종료한다.
 * 
 * If the delimiter is found, it is extracted and discarded
 * (i.e. it is not stored and the next input operation
 * will begin after it).
 * => 입력 시 delim 이전의 문자는 버려진다. 예를 들어
 * delim이후의 문자가 다음 입력에 사용된다.
 * 
 * Note that any content in str before the call 
 * is replaced by the newly extracted sequence.
 * 
 * Each extracted character is appended to the string 
 * as if its member push_back was called.
 * 
 * # 리턴값
 * parameter와 동일한 istream의 참조를 반환.
 * - 리턴값을 통한 입력 성공 실패 여부를 판단한 수 없기 때문에
 * 이외의 구별 방법이 필요. 이 때 활용할 수 있는 것이
 * " ios_base::iostate "
 * => stream error state flag를 나타내는 bitmask type
 * 
 * getline()은 호출될 때 istream의 내부적인 상태 비트를
 * 변경한다. (eofbit, failbit, badbit, goodbit(0))
 * 
 * # stream error state flag 확인 방법
 * ios::rdstate
 * Get error state flags (public member function )
 * 
 * ios::setstate
 * Set error state flag (public member function )
 * 
 * ios::good
 * Check whether state of stream is good (public member function )
 * 
 * ios::bad
 * Check whether badbit is set (public member function )
 * 
 * ios::fail
 * Check whether either failbit or badbit is set (public member function )
 * 
 * ios::eof
 * Check whether eofbit is set (public member function )
 * 
 * Ref) http://www.cplusplus.com/reference/string/string/getline/
 */

#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;

int main()
{
    string s;

    // (1) 테스트 
    // 기본 delim인 개행 이외의 문자를 구분자로 지정하여
    // 사용할 경우, 지정한 구분자 이후의 개행 문자가
    // 이후 입력에 영향을 주기 때문에 유의!
    getline(cin, s, 'c');
    cout << s << endl;

    // (2) 테스트
    getline(cin, s);
    cout << s << endl;

    // iostate는 입력 성공 시 0으로 세팅됨.
    cout << cin.rdstate() << endl;

    while(!cin.eof())
    {
        getline(cin, s);
        cout << s << endl;
    }
    cout << cin.eof() << endl;
    
}