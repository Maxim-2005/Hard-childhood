#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int A = 0;
	int B = 0;
	int temp = 0;
	
	cout << "������� ����� �: " << endl;
	cin >> A;
	cout << "������� ����� B: " << endl;
	cin >> B;
	
	temp = A;
	A = B;
	B = temp;

	cout << "������ ����� � �������������� ����������: " << endl;
	cout << "�: ";
	cout << A << endl;
	cout << "B: ";
	cout << B << endl;


	A ^= B ^= A ^= B;
	cout << "������ ����� ��� �������������� ����������: " << endl;
	cout << "�: ";
	cout << A << endl;
	cout << "B: ";
	cout << B << endl;
}