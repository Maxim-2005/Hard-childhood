# Задание №1 Выскокстный год

#Импорт рандома
import random

#Создание переменных
x = 0
y = 0

#Создание рандомного числа
x = (random.randint(0, 101))

#Цикл
while x != y:
#Логика
	y = input("Попробуйте угадать число: ") #Запрос числа
	
	if (int(y)) > (int(x)):
		print("Меньше")
	elif (int(y)) < (int(x)):
		print("Больше")
		
	else:
		print("Вы угодали число: ", x)
	
input()
