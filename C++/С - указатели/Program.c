#include <stdio.h>
#include <locale.h>

int main(void)
{
	setlocale(LC_ALL, "RUS");

	int x = 727;
	printf("Значение переменной : %d\n", x);
	printf("Адрес в памяти : %p\n", &x);
	int* p = &x;
	printf("Адрес указателя : %p\n", p);
	printf("Значение по указателяю : %d\n", *p);
	p++;
	printf("Переход по памяти : %p\n", p);
	printf("Вывод мусора : %d\n", p);

	system("pause>nul");
	return 0;
}