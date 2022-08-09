// ВУЗ_15.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main() 
{
    setlocale(LC_ALL, "RUS");
    m:
    srand(time(NULL));
    int n, t, a, b;
    a = 0;
    b = 0;
    n = rand() % 100;
    cout << "Введите число: ";

    for (int i = 0; i <= 4; i++) {
        cin >> t;
        if (t > n) {
            cout << "Загаданное число меньше" << endl;
        } 
        else if (t < n) {
            cout << "Загаданное число больше" << endl;
        } 
        else {
            cout << "Поздравляю! Вы угадали " << n << endl;
            b = 1;
            break;
        }
    }
    
    if (b == 0) {
        cout << "Вы проиграли. Было загадано : " << n << endl;
    }
    cout << "Хотите начать сначала ? (1 - ДА)" << endl;
    cin >> a;
    if (a == 1) {
        goto m;
    }
}