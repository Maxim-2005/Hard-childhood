# Задание №1 Выскокстный год

while True:
	x = int(input("Введите год: "))
	 
	if x % 4 == 0 and x % 100 != 0 or x % 400 == 0: 
		print("Высокостный")
	else:
		print("Обычный")

input()