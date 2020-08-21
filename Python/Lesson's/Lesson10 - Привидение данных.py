# Урок номер 10 Привидение данных

# Int - int - int
def int_int_int(x):
	print("Ввод: ", x, " - Тип данных: ", type(x))
	res = x*2
	return res

res = int_int_int(100)
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Str - str - str
x = "200"
print("Ввод: ", x, " - Тип данных: ", type(x))
res = x+x
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Int - int - str
x = 380
print("Ввод: ", x, " - Тип данных: ", type(x))
res = str(x//10) + " Попугаев"
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Int - str - str
x = 123
print("Ввод: ", x, " - Тип данных: ", type(x))
res = str(x)[::-1]
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Int - str - int
x = 89
print("Ввод: ", x, " - Тип данных: ", type(x))
res = int(str(x)[::-1])
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Str - str - int
x = "12345"
print("Ввод: ", x, " - Тип данных: ", type(x))
res = int(x+x)
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Str - int - str
x = "12345"
print("Ввод: ", x, " - Тип данных: ", type(x))
res = str(int(x)*2)
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

# Str - int - int
x = "12345"
print("Ввод: ", x, " - Тип данных: ", type(x))
res = int(x)*3
print("Вывод: ", res, " - Тип данных: ", type(res))
print()

input()
