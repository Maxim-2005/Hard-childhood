# Урок номер 3 логика

x = True
y = False
print(x == y)
print("")

x = 5
y = 6
z = x == y
print(z)
print(type(z))
print("")

print(x != y)
print(x > y)
print(x <= y)
print("")

print(x > 0 and y > 0)
print(x < 0 or y < 0)
print(not x == y)
print("")

x = 10
if x > 0:
	print("Число", x, "-Больше нуля")
	if x == 10:
		print("ЦОЙ ЖИВ!")
elif x == 0:
	print("Число равно 0", x)
else:
	print("Число меньше 0", x)
print("")

if 5 < x < 15:
	print("Двойное сравнение " + str(x))
print("")

print(all([1, 125, "x", "abc", "True", 2<1, 0]))
print(any([1, 0, "", "", "False", 2>10]))
print("yes" if 5 < 2 else print("no"))
if all ([5 > 3, 1 > 0, 10 < 11, 2 > 3]):
        print("yes")
else:
        print("no")
input()
