N = int(input())
M = 0
L = 1
R = 1

while N > 0:
    S = R * 9 * L
    if N < S:
        M += N // L
        break
    else:
        N -= S
        M += S // L
        L += 1
        R *= 10

print(M)

#Дорешивание
