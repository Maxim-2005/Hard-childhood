# Урок номер 5 Функции

# Функция мЭин
def Main():
	HW()
	HW_Name("Maxim")
	HW_Name_Plus("Test")
	HW_Name_Plus()
	Name_Age("Maxim1", 14)
	Name_Age(14, "Maxim2")
	Name_Age(name = "Maxim3", age = 14)
	Name_Age(age = 14, name = "Maxim4")
	Summ(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
	x = Summ_Return(1, 2, 3)
	print(x)
	Name, Age = Return_Lot()
	print(Name, Age)
	print(Return_Lot())

# Простая функция
def HW():
	print("Hello World")
	print("")

# Функция с параметром
def HW_Name(x):
	print("Hello", x)
	print("")

# Функция с параметром по умолчанию
def HW_Name_Plus(x = "Пользователь"):
	print("Hello", x)
	print("")

# Функция с именованными параметрами
def Name_Age(name, age):
	print("Имя:", name, "|", "Возраст:", age)
	print("")

# Функция с множеством параметров
def Summ(*params):
	S = 0
	for i in params:
		S += i
	print("Сумма:", S)
	print("")

# Функция с рЭтурном
def Summ_Return(*params):
	S = 0
	for i in params:
		S += i
	return S

# Функция с несколькоми возвратами
def Return_Lot():
	name = "Barak Obama"
	age = 89
	return name, age

Main()

input()

def calc(x, y):
        yield(x + y)
        yield(x - y)
        yield(x * y)
        yield(x / y)

for i in calc(2, 3):
        print(i)

input()
