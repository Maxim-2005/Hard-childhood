print("1 - ввод параметров треугольника через длины сторон или 2 - ввод параметров через координаты вершин или другое целое число по модулю не более 1000: ");
t = float(input());
if t > 2:
    print("Ошибочный ввод");

elif t == 1:
    print("Введите число А: ");
    a = float(input());
    print("Введите число B: ");
    b = float(input());
    print("Введите число C: ");
    c = float(input());

    p = (a + b + c) / 2;
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5;

    if a > 1000 or b > 1000 or c > 1000 or a > b + c or b > c + a or c > b + a:
        print("Ошибочный ввод");
    
    elif S > 0:
        print("S = ", S);
    
    else:
        print("Ошибочный ввод");    
    

else:
    print("Введите координаты точки А: ");
    a, a2 = map(float, input().split());
    print("Введите координаты точки B: ");
    b, b2 = map(float, input().split());
    print("Введите координаты точки C: ");
    c, c2 = map(float, input().split());

    t1 = ( (abs(a2 - a) ** 2) + (abs(b2 - b) ** 2) ) ** 0.5;
    t2 = ( (abs(b2 - b) ** 2) + (abs(c2 - c) ** 2) ) ** 0.5;
    t3 = ( (abs(c2 - c) ** 2) + (abs(a2 - a) ** 2) ) ** 0.5;

    p = (t1 + t2 + t3) / 2;
    S = (p * (p - t1) * (p - t2) * (p - t3)) ** 0.5;

    if a > 1000 or b > 1000 or c > 1000 or a2 > 1000 or b2 > 1000 or c2 > 1000 or t1 > t2 + t3 or t2 > t3 + t1 or t3 > t2 + t1:
        print("Ошибочный ввод");

    elif S > 0 :
        print("S = ", S);
    
    else:
        print("Ошибочный ввод");
