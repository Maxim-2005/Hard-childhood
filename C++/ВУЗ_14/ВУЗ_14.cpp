// ВУЗ_14.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;


int main()
{
    int n, t = 0;
    cin >> n;

    for (int i = 0; i <= n; i++) {
        if (pow(2, i) >= n) {
            break;
        }
        else {
            t++;
        }
    }
    cout << t;  
}