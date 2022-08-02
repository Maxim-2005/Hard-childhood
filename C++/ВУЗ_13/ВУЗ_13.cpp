// ВУЗ_13.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    int n, t = 0;
    cin >> n;

    if (2 > n || n > 1e9) {
        cout << "Некорректные данные";
    }
    else {
        for (int i = 2; i <= sqrt(n); i++)
            if (n % i == 0)
                t++;
    }
    if (t == 0) {
        cout << "Простое";
    } else {
        cout << "Составное";
    }

    system("pause>nul");
    return 0;
}