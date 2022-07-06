def digitize(n):
    n = str(n)
    y = n[::-1]
    x = list(map(int, y))
    
    return x

#Для локального запуска
print(digitize(348597))
input()
