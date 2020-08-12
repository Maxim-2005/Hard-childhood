def disemvowel(string):
    string = list(string)
    s = ""
    for i in string:
        if not (i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            s += i
    return s

# Для локальног запуска
print(disemvowel("Test one"))
input()