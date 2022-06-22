print("Введите выражение: ");
x, z, y = input().split();
x = float(x);
y = float(y);

if z == '*' :
    print(x * y);

elif (z == '+'):
    print(x + y);

elif (z == '-'):
    print(x - y);

elif (z == '/'):
    print(x / y);

else:
    print("НЕДОСТУПНОЕ ВЫРАЖЕНИЕ");

