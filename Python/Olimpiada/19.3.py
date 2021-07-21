N, M = map(int, input().split())
arr = list(map(int, input().split()))
Maximum = 0

for i in arr:
    Y = arr.count(i)
    if Y > Maximum:
        Maximum = Y
if M <= Maximum:
    print(0)
else:
    print(M - Maximum)