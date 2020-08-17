def high_and_low(numbers):
        numbers = numbers.split()
        arr = []
        for i in range(len(numbers)):
                arr.append(int(numbers[i]))
        smax = str(max(arr))
        smin = str(min(arr))
        return smax + " " + smin

# Для локального запуска
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
input()
