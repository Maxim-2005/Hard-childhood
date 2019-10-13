//Игра больше меньше
//Автор Покидько Максим
//11.8.2018
//Крым Саки
#include <iostream>
#include <ctime>
using namespace std;
void main()
{
start1:
//Старт программы +
//Создание рандомного числа +
	srand(time(NULL));
	int N = 0, num;
	int num1;
	num = rand() % 1000 + 1;
start:
setlocale(LC_ALL, "RUS");
system("title Больше Меньше");

//Описание игры +

//Запрос цифры от 1 до 1000 +
	cout << "Введите число от 1 до 1000\n";
	cin >> num1;
	system("cls");
	N++;
//Вывод Вы угодакли число +
	if (num == num1)
	{
		cout << "Вы угадали число c \n" << N << " попыток.\n";
	}
//Вывод Больше +
	if (num > num1)
	{
		cout << "Больше\n";
	}
//Вывод Меньше +
	if (num < num1)
	{
		cout << "Меньше\n";
	}
//На старт +
	goto start;
	system("pause>nul");
}