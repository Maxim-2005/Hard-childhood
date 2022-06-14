// ВУЗ_05.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main(){
	setlocale(LC_ALL, "RUS");
	double x;
	double t;
	double u;
	double g = 9.8;

	cout << "Введите число x: " << endl;
	cin >> x;
	cout << "Введите число u: " << endl;
	cin >> u;
	cout << "Введите число t: " << endl;
	cin >> t;

	cout << x + (u * t) - (g * (t * t) / 2);
}