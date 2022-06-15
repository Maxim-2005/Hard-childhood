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

    //Умножение
    __asm
    {
        mov eax, x
        mov ebx, y
        mul ebx
        mov res, eax
    }
    cout << res;

    //Вычитание
    cin >> x;
    cin >> y;
    __asm
    {
        mov eax, x
        mov ebx, y
        sub eax, ebx
        mov res, eax
    }
    cout << res;

   //Деление
   cin >> x;
   cin >> y;
   __asm
   {   mov edx, 0
       mov eax, x
       mov ebx, y
       div ebx
       mov res, eax
   }
   cout << res;
   system("pause > nul");
}