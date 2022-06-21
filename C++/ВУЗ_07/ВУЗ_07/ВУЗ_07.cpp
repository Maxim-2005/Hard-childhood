// ВУЗ_07.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	double t, t1, t2, t3, a, b, c, a2, b2, c2, S, p;
	cout << "1 - ввод параметров треугольника через длины сторон или 2 - ввод параметров через координаты вершин или другое целое число по модулю не более 1000: ";
	cin >> t;
	if (t > 2) {
		cout << "Ошибочный ввод";
	}
	else if (t == 1) {
		cout << "Введите число a: " << endl;
		cin >> a;
		cout << "Введите число b: " << endl;
		cin >> b;
		cout << "Введите число c: " << endl;
		cin >> c;
		
		p = (a + b + c) / 2;
		S = sqrt(p * (p - a) * (p - b) * (p - c));

		if (a > 1000 || b > 1000 || c > 1000) {
			cout << "Ошибочный ввод";
		}
		else if (S > 0) {
			cout << "S = " << S;
		}
		else {
			cout << "Ошибочный ввод";
		}
	}
	else {
		cout << "Введите координаты точки a: " << endl;
		cin >> a;
		cin >> a2;
		cout << "Введите координаты точки b: " << endl;
		cin >> b;
		cin >> b2;
		cout << "Введите координаты точки c: " << endl;
		cin >> c;
		cin >> c2;

		t1 = sqrt( (abs(a2 - a) * abs(a2 - a)) + (abs(b2 - b) * abs(b2 - b)) );
		t2 = sqrt( (abs(b2 - b) * abs(b2 - b)) + (abs(c2 - c) * abs(c2 - c)) );
		t3 = sqrt( (abs(c2 - c) * abs(c2 - c)) + (abs(a2 - a) * abs(a2 - a)) );

		p = (t1 + t2 + t3) / 2;
		S = sqrt(p * (p - t1) * (p - t2) * (p - t3));

		if (a > 1000 || b > 1000 || c > 1000 || a2 > 1000 || b2 > 1000 || c2 > 1000) {
			cout << "Ошибочный ввод";
		}
		else if (S > 0) {
			cout << "S = " << S;
		}
		else {
			cout << "Ошибочный ввод";
		}
	}

	system("pause>nul");
	return 0;
}