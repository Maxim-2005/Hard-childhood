#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int A = 0;
	int B = 0;
	int temp = 0;
	
	cout << "Введите число А: " << endl;
	cin >> A;
	cout << "Введите число B: " << endl;
	cin >> B;
	
	temp = A;
	A = B;
	B = temp;

	cout << "Замена чисел с дополнительной переменной: " << endl;
	cout << "А: ";
	cout << A << endl;
	cout << "B: ";
	cout << B << endl;


	A ^= B ^= A ^= B;
	cout << "Замена чисел без дополнительной переменной: " << endl;
	cout << "А: ";
	cout << A << endl;
	cout << "B: ";
	cout << B << endl;
}