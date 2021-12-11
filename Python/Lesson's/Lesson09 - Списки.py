# Урок номер 9 списки

x = "Hello world!"
print("конвертация строки в массив -", list(x))
x = []
print("создание пустого списка -", x)
x.append(123)
x.append(456)
print("добавляем в конец списка -", x)
y = ["abc", "deg"]
print("создание списка с данными -", y)
x.extend(y)
print("добавляем список в cписок -", x)
x.insert(2, "000000")
print("вставляем элемент в позицию cписка -", x)
x.append(123)
x.remove(123)
print("удаляем один элемент из cписка -", x)
x.pop(1)
print("вырезаем позицию с элементом из cписка -", x)
y = x.copy()
print("копируем список (не ссылку) -", y)
y.clear()
print("очищаем список -", y)
print()

print("ищем позицию элемента -", x.index(456))
print("ищем позицию элемента от позиции -", x.index(123, 2))
print("ищем позицию элемента в диапазоне -", x.index("abc", 1, 4))
print("подсчет совпадений в списке -", x.count(123))
print()

x = [1, 3, 5, 10, 2]
x.sort()
print("сортировка списка -", x)
x.reverse()
print("переворот списка -", x)
print()

print("срез списка от ... -", x[2:])
print("срез списка до ...-", x[:2])
print("срез списка от и до -", x[1:3])
print("срез списка от и до с шагом -", x[::2])
print()

for i in x:
    print("обход списка циклом -", i)

for i in range(len(x)):
    print("индекс списка -", i, " и его значение - ", x[i])
print()

x = [i * 3 for i in "Hello"]
print("генератор списка циклом -", x)
x = [i * 4 for i in "Hello" if i != "l"]
print("генератор списка циклом с условием -", x)

arrname = ["maxim", "nikita", "matvey"]
arrage = [16, 14, 12]
arryear = [2005, 2007, 2009]
arr = list(zip(arrname, arrage, arryear))

for name, age, year in zip(arrname, arrage, arryear):
    print(name, age, year)

a, b, c = zip(*arr)
print(a, b, c)

input()
