# Задание №1 Выскокстный год

x = input("Введите год: ")
 
if (int(x) % 4) and (int(x) % 100) and (int(x) % 400) > 0:
	print("Невысокостный")
else:
	print("Высокостный")

input()