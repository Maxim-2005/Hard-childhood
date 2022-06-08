// Бинарные операции.cpp

#include <iostream>
#include <bitset>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");
    int x = 0b0011; //3
    int y = 0x5; //5
    int z;

    cout << "x = " << x <<  ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;

    cout << endl;
    cout << "Логическое не: " << endl;
    x = ~x;
    y = ~y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;

    cout << endl;
    cout << "Логическое и: " << endl;
    x = 3;
    y = 5;
    z = x & y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;

    cout << endl;
    cout << "Логическое или: " << endl;
    z = x | y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;

    cout << endl;
    cout << "Логическое исключающее или: " << endl;
    z = x ^ y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;

    cout << endl;
    cout << "Логическое побитовый сдвиг в право: " << endl;
    x = 3;
    y = x >> 1;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;

    cout << endl;
    cout << "Логическое побитовый сдвиг в лево: " << endl;
    x = 3;
    y = x << 1;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;

    x &= y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;

    system("pause > nul");
    return 0;
}