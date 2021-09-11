def solution(number):
    n = 0
    if number <= 0:
        return 0
    else:
        for i in range(number):
            if (i % 3 == 0) or (i % 5 == 0):
                n = n + i
    return n

#Для локального запуска
print(solution(10))
input()