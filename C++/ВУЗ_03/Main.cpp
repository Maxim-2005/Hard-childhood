#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int A1 = 0;
	int B1 = 0;

	cout << "Введите число А: ";
	cin >> A1;
	cout << "Введите число B: ";
	cin >> B1;

	cout << "A + B: " << A1 + B1 << endl;
	cout << "A - B: " << A1 - B1 << endl;
	cout << "A * B: " << A1 * B1 << endl;
	if (B1 == 0)
		cout << "На 0 делить нельзя" << endl;
	else
		cout << "A / B: " << A1 / B1 << endl;

	double A2 = 0;
	double B2 = 0;

	cout << "Введите число А: ";
	cin >> A2;
	cout << "Введите число B: ";
	cin >> B2;

	cout << "A + B: " << A2 + B2 << endl;
	cout << "A - B: " << A2 - B2 << endl;
	cout << "A * B: " << A2 * B2 << endl;
	if (B2 == 0)
		cout << "На 0 делить нельзя" << endl;
	else
		cout << "A / B: " << A2 / B2 << endl;

	int A3 = 0;
	double B3 = 0;

	cout << "Введите число А: ";
	cin >> A3;
	cout << "Введите число B: ";
	cin >> A3;

	cout << "A + B: " << A3 + B3 << endl;
	cout << "A - B: " << A3 - B3 << endl;
	cout << "A * B: " << A3 * B3 << endl;
	if (B3 == 0)
		cout << "На 0 делить нельзя" << endl;
	else
		cout << "A / B: " << A3 / B3 << endl;

	double A4 = 0;
	int B4 = 0;

	cout << "Введите число А: ";
	cin >> A4;
	cout << "Введите число B: ";
	cin >> B4;

	cout << "A + B: " << A4 + B4 << endl;
	cout << "A - B: " << A4 - B4 << endl;
	cout << "A * B: " << A4 * B4 << endl;
	if (B4 == 0)
		cout << "На 0 делить нельзя" << endl;
	else
		cout << "A / B: " << A4 / B4 << endl;

	system("pause>nul");

	return 0;
}