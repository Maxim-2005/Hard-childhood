# Задание №1 Выскокстный год
import os

os.system("mode con cols=40 lines=10")

while True:
	x = int(input("Введите год: "))
	os.system("cls||clear")
	if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
		print("Высокостный")
	else:
		print("Обычный")

input()