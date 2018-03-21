/*
 * http://en.cppreference.com/w/cpp/utility/bitset/bitset
 * 
 * Parameters
 * val	-	number used to initialize the bitset
 * str	-	string used to initialize the bitset
 * pos	-	a starting offset into str
 * n	-	number of characters to use from str
 * one	-	alternate character for set bits in str
 * zero	-	alternate character for unset bits in str
 * 
 */

#include <bitset>
#include <string>
#include <iostream>
#include <climits>

using namespace std;

int main() 
{
    // empty constructor
    sbitset<8> b1; // [0,0,0,0,0,0,0,0]
 
    // unsigned long long constructor
    bitset<8> b2(42);          // [0,0,1,0,1,0,1,0]
    bitset<70> bl(ULLONG_MAX); // [0,0,0,0,0,0,1,1,1,...,1,1,1] in C++11
    bitset<8> bs(0xfff0);      // [1,1,1,1,0,0,0,0]
 
    // string constructor
    string bit_string = "110010";
    bitset<8> b3(bit_string);       // [0,0,1,1,0,0,1,0]
    bitset<8> b4(bit_string, 2);    // [0,0,0,0,0,0,1,0]
    bitset<8> b5(bit_string, 2, 3); // [0,0,0,0,0,0,0,1]
 
    // string constructor using custom zero/one digits
    string alpha_bit_string = "aBaaBBaB";
    bitset<8> b6(alpha_bit_string, 0, alpha_bit_string.size(),
                      'a', 'B');         // [0,1,0,0,1,1,0,1]
 
    // char* constructor using custom digits
    bitset<8> b7("XXXXYYYY", 8, 'X', 'Y'); // [0,0,0,0,1,1,1,1]
 
    cout << b1 << '\n' << b2 << '\n' << bl << '\n' << bs << '\n'
         << b3 << '\n' << b4 << '\n' << b5 << '\n' << b6 << '\n'
         << b7 << '\n\n\n';

    bitset<8> b8("10010");
    for(int i=0; i<b8.size(); i++){
        printf("%d : %d\n", i, b8[i])
    }

    b8.test(5);
    cout << b8 << '\n';

    b8.set(0);
    b8.set(6);
    cout << b8 << '\n';

    b8.reset(0);
    cout << b8 << '\n';

    b8.flip(1);
    cout << b8 << '\n';

    
}