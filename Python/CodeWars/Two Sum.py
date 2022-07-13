def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(numbers[i] + numbers[j], target)
                return [i, j]


#Для локального запуска
print(two_sum([1,2,3], 4));

