s, l1, r1, l2, r2 = map(int, input().split());

if 1e15 <= abs(s) or 1e15 <= abs(l1) or 1e15 <= abs(r1) or 1e15 <= abs(l2) or 1e15 <= abs(r2) or l1 >= r2 or l2 >= r2:
    print("Некорректный ввод: ")
if l1 + l2 > s or r1 + r2 < s:
    print(-1)
elif s - l1 < r2:
    print(l1, s - l1)
else:
    print(r2, s - r2)
