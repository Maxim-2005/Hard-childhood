# Задание номер 6 Камень ножнецы бумага

import os
import random

n = 0
v = 0
d = 0
p = 0
g = 0

while True:
	x = int(input("Введите 1-Кмень, 2-Ножнецы, 3-Бумага: "))
	y = random.randint(1, 4)

	if x == y:
		print("Ничья")
		g = "Ничья"
		n +=1
		v += 1
		
	elif x == 1 and y == 3:
		print("Победа")
		g = "Победа"
		p += 1
		v += 1
		
	elif x == 2 and y == 3:
		print("Победа")
		g = "Победа"
		p += 1
		v += 1
		
	elif x == 3 and y == 2:
		print("Победа")
		g = "Победа"
		p += 1
		v += 1
	else:
		print("Поражение")
		g = "Поражение"
		d += 1
		v += 1
	os.system("cls||clear")
	print("Победа: ", p, "Поражение: ", d, "Ничья: ", n, "Всего игры: ", v)
	print("Результат игры: ", g)
input()