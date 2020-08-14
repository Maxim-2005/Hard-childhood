# Урок номер 7 Операторы

x = 5 #input("Ввод в консоль - ")
print("Конвертация в число", int(x))
print("Конвертация в дробное", float(x))
print()

x = "Hello World"
print("Длина строки", len(x))
print("Конвертация в строку", str(len(x))+"ед")
print("Трансформация в список", list(x))
print("Трансформация в картеж", tuple(x))
print()

colors = [("Красный", 2), ("Зеленый", 1), ("Синий", 3), ("Фиолетовый", 5)]
print("Список картежей", colors)

colors = dict(colors)
print("Трансформация в словарь", colors)
print()

x = [1, 5, 7, 3, 9, 4, 0, 2, 8, 6, 1, 5, 7]
print("Список", x)
print("Минимальное значение", min(x))
print("Максимальное значение", max(x))
print("Сортировка списка", sorted(x))
print("Обратная сортировка списка", sorted(x, reverse = True))
print("Сумма списка", sum(x))
print("Сумма цифр", sum([1, 2, 3, 4, 5]))
print("Сумма цикла списка", sum(i**2 for i in x))
print()

print("Набор", set(x))
print("Фиксированный набор", frozenset(x))
print()

print("Bool любого числа", bool(-125))
print("Bool 0", bool(0))
print("Bool любого знака", bool("Hi"))
print("Bool пробела", bool(""))


input()