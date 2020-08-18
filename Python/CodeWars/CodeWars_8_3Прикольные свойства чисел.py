def dig_pow(n, p):
	n = str(n)
	x = 0
	for i in n:
		x += int(i)**p
		p += 1
	if x % int(n) == 0:
		return x // int(n)
	return -1

#Для локального запуска
print(dig_pow(89, 1))
input()