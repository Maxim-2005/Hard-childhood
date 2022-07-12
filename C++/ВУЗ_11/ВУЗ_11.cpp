// ВУЗ_11.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    int a, b, t;

    cin >> a >> b;
    t = a;

    for (int i = 1; i < b; i++)
    {
        t *= a;
    }
    cout << t << endl;

    system("pause>nul");
    return 0;
}