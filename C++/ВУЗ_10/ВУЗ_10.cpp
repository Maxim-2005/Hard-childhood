// ВУЗ_10.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    int s, l1, r1, l2, r2;

    cin >> s >> l1 >> r1 >> l2 >> r2;


    if (1e15 <= abs(s) || 1e15 <= abs(l1) || 1e15 <= abs(r1) || 1e15 <= abs(l2) || 1e15 <= abs(r2) || l1 >= r2 || l2 >= r2) 
    {
        cout << "Некорректный ввод: ";
        system("pause>nul");
        return 0;
    }

    if (l1 + l2  > s || r1 + r2 < s) 
    {
        cout << -1;
    }
    else if (s - l1 < r2) 
    {
        cout << l1 << s - l1;
    }
    else 
    {
        cout << r2 << s - r2;
    }

    system("pause>nul");
    return 0;
}