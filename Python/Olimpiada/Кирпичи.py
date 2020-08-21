def brick(z):
	A1, B1, A2, B2 = input().split()

        A1 = int(A1)
        B1 = int(B1)
        A2 = int(A2)
        B2 = int(B2)

        if A1 > B1:
             z1 = A1
        else:
             z1 = B1

        if A2 > B2:
             z2 = A2
        else:
             z2 = B2

        h = int(z1) + int(z2)

        return h

# Для локального запуска
print(brick("1 3 2 2")) # 5
input()
