import random
a = 1

while a == 1:
    n = random.randint(0, 100)
    a = 0;
    b = 0;
    print("Введите число: ")

    for i in range(5):
        t = int(input())
        if t > n:
            print("Загаданное число меньше")
        elif t < n:
            print("Загаданное число больше")
        else:
            print("Поздравляю! Вы угадали ", n)
            b = 1
            break;

    if b == 0:
        print("Вы проиграли. Было загадано : ", n)
    print("Хотите начать сначала ? (1 - ДА)")
    a = int(input())
