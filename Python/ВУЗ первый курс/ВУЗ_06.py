print("Введите число a: ");
a = float(input());
print("Введите число b: ");
b = float(input());
print("Введите число c: ");
c = float(input());

d = (b * b) - 4 * a * c;

if (a == 0):
        print("x: ", (-c / b));
elif (d > 0):
        print("x1: "(-b + sqrt(d)) / (2 * a));
        print("x2: "(-b - sqrt(d)) / (2 * a));
elif (d == 0):
        print("x: ", -b / (2 * a));
else:
        print("Нет корней");

