// ВУЗ_12.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;


int main()
{
    int x, t = 1;

    cin >> x;

    for (int i = 1; i <= x; i++) {
        t *= i;
    }
    cout << t;
}