/*
 * Sets the decimal precision to be used to format 
 * floating-point values on output operations.
 * 
 * Behaves as if member precision were called with 
 * n as argument on the stream on which it is 
 * inserted/extracted as a manipulator 
 * (it can be inserted/extracted on input streams or 
 * output streams).
 * 
 * This manipulator is declared in header <iomanip>.
 * 
 *  - ios_base::precision
 * Get/Set floating-point decimal precision (public member function )
 * 
 * - fixed
 * Use fixed floating-point notation (function )
 * 
 * - scientific
 * Use scientific floating-point notation (function )
 * 
 * Ref) http://www.cplusplus.com/reference/iomanip/setprecision/
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double f = 12345678.987654321;
    cout << f << endl;
    cout << setprecision(5) << f << endl;
    cout << setprecision(6) << f << endl;
    cout << setprecision(7) << f << endl;
    cout << setprecision(8) << f << endl;
    cout << setprecision(9) << f << endl;
    cout << setprecision(10) << f << endl;
    cout << f << endl << endl;

    cout << fixed << setprecision(6) << f << endl;
    cout << fixed << setprecision(7) << f << endl;
    cout << fixed << setprecision(8) << f << endl;
    cout << fixed << setprecision(9) << f << endl;
    cout << f << endl;

    return 0;
}