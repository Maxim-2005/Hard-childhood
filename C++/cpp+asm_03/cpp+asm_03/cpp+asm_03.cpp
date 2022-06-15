#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");

    int count;
    int factorial = 1;

    cout << "Введите число для расчета факториала: " << endl;
    cin >> count;

    //Умножение
    __asm
    {
        mov esi, 1
        mov eax, factorial
        label:                                  ;Метка для повтора
            mul esi
            inc esi
        cmp esi, count
        jng label                              ;Крутимся в цикле
        mov factorial, eax
    }
    cout << factorial;
    system("pause > nul");
}