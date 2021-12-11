# Урок номер 4 Цыклы
import random

x = 0
while x < 3:
	x += 1
	print(x)
print("")
	
game_over = False
while not game_over:
	x += 1
	if x > 6:
		game_over = True
	print(x)
print("")

#Циклы For : Stop, Start-stop, Start-stop-step
for i in range(5):
	print(i)
print("")

for i in range(10, 13):
	print(i)
print("")

for i in range(100, 200, 20):
	print(i)
print("")

x = [-10, -5, 20, 100, 5000]
print(x)
print(type(x))
for i in x:
	print(i)
print("")
	
for i in"Hello World":
	print(i)
print("")

#Вложенные циклы
for i in range(1, 11):
	for j in range(1, 11):
		print(i * j, end = "  ")
	print("")

#break and continue
x = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(x)
random.shuffle(x)
print(x)
while True:
	print("Рандом от 0 до 1 - ", random.random())
	print("Рандом от 100 до 200 - ", random.randint(100, 200))
	print("Рандом рэндже до 10 - ", random.randrange(10))
	print("Рандом рэндже от 1000 до 2000 - ", random.randrange(1000, 2000))
	print("Рандом рэндже от 90 до 180 / 3 - ", random.randrange(90, 180, 3))
	print("Рандом из списка - ", random.choice(x))
	y = input("Выйти - 0, Продолжить - 1: ")
	if y == "0":
		break
	else:
		continue

arr = ["one", "two", "three", "four", "five"]

for i, value in enumerate(arr):
        print(i, value)

iArr = iter(reversed(arr))
print(next(iArr))
print(next(iArr))
print(next(iArr))
print(next(iArr))
print(next(iArr))

input()
