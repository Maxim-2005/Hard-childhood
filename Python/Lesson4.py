# Урок номер 4 Цыклы

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

input()