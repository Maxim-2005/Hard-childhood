// ВУЗ_08.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    double x, y;
    char z;

    cout << "Введите выражение: " << endl;
    cin >> x >> z >> y;

    if (z == '*') {
        cout << x * y;
    }
    else if (z == '+') {
        cout << x + y;
    }
    else if (z == '-') {
        cout << x - y;
    }
    else if (z == '/') {
        cout << x / y;
    }
    else {
        cout << "НЕДОСТУПНОЕ ВЫРАЖЕНИЕ";
    }

    system("pause>nul");
    return 0;
}