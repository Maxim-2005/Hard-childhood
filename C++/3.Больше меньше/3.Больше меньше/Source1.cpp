//���� ������ ������
//����� �������� ������
//11.8.2018
//���� ����
#include <iostream>
#include <ctime>
using namespace std;
void main()
{
start1:
//����� ��������� +
//�������� ���������� ����� +
	srand(time(NULL));
	int N = 0, num;
	int num1;
	num = rand() % 1000 + 1;
start:
setlocale(LC_ALL, "RUS");
system("title ������ ������");

//�������� ���� +

//������ ����� �� 1 �� 1000 +
	cout << "������� ����� �� 1 �� 1000\n";
	cin >> num1;
	system("cls");
	N++;
//����� �� �������� ����� +
	if (num == num1)
	{
		cout << "�� ������� ����� c \n" << N << " �������.\n";
	}
//����� ������ +
	if (num > num1)
	{
		cout << "������\n";
	}
//����� ������ +
	if (num < num1)
	{
		cout << "������\n";
	}
//�� ����� +
	goto start;
	system("pause>nul");
}