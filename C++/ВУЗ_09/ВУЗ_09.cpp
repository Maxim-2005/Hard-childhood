// ВУЗ_09.cpp

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    int h1, m1, h2, m2, t;
    char z;

    cout << "Введите время прихода 1 человека: " << endl;
    cin >> h1 >> z >> m1;
    cout << "Введите время прихода 2 человека: " << endl;
    cin >> h2 >> z >> m2;

    if (h1 < 0 || h1 > 23 || h2 < 0 || h2 > 23 || m1 < 0 || m1 > 59 || m2 < 0 || m2 > 59) {
        cout << "Не корректный ввод: ";
        system("pause>nul");
        return 0;
    }

    t = abs((h2 * 60 + m2) - (h1 * 60 + m1));

    if (t < 15 || t >= 1425) {
        cout << "Встреча состоится : " << endl;
    }
    else {
        cout << "Встреча не состоится : " << endl;
    }

    system("pause>nul");
    return 0;
}