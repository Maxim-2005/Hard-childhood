import math;

n = int(input());
t = 0;

if 2 > n or n > 1000000000:
    print("Некорректные данные");
else:
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            t += 1;
if t == 0:
    print("Простое");
else:
    print("Составное");
