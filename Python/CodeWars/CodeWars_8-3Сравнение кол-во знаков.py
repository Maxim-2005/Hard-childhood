def xo(s):

	x = s.count("x") + s.count("X")
	o = s.count("o") + s.count("O")

	if x == o:
		return True
	else:
		return False

# Для локальног запуска
print(xo("ooxXm"))
input()