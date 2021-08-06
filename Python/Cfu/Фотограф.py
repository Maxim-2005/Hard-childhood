# Фотограф

#ВВОД
N = 10 #input("Введите диапозон номеров")
M =  7 #input("Сколько всего номеров")
arr = "1 3 6 4 3 2 9" #input("Вводим массив")
arr = arr.split()
setArr = set(arr)

#РЕШЕНИЕ
sumN = 0
for i in setArr:
	temp = arr.count(i)
	if temp > sumN:
		maxN = i
		sumN = temp
	elif temp == sumN and int(maxN) > int(i):
		maxN = i
#ВЫВОД
print(maxN, sumN)

input()