// ВУЗ_05.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	double a, b, c, d;
	cout << "Введите число a: " << endl;
	cin >> a;
	cout << "Введите число b: " << endl;
	cin >> b;
	cout << "Введите число c: " << endl;
	cin >> c;

	d = (b * b) - 4 * a * c;

	if (a == 0)
	{
		cout << "x: " << (-c / b) << endl;
	}
	else if (d > 0)
	{
		cout << "x1: " << (-b + sqrt(d)) / (2 * a) << endl;
		cout << "x2: " << (-b - sqrt(d)) / (2 * a) << endl;
	}
	else if (d == 0)
	{
		cout << "x: " << -b / (2 * a) << endl;
	}
	else
	{
		cout << ("Нет корней");
	}

	system("pause>nul");
	return 0;
}