# Задание 3 периметр и площадь

import os
import math

x = 0
y = 0
z = 0
i = 0

while i < 1:
	os.system("cls||clear")
	x = int(input("Введите длинну: "))
	y = int(input("Введите ширину: "))

	z = math.sqrt((x**2 + y**2))
	print("Гипотенуза", z )
	print("Периметр", z + x + y)
	print("Площадь", (x * y)/2)
	input()
