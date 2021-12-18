#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");
    
    int x;
    int y;
    int res;

    cin >> x;
    cin >> y;

    __asm
    {
        mov eax, x
        mov ebx, y
        add eax, ebx
        mov res, eax
    }

    // Повторное использование данных

    cout << res;
    cin >> x;
    __asm
    {
        mov eax, x
        //mov ebx, y
        add eax, ebx
        mov res, eax
    }

    cout << res;
}