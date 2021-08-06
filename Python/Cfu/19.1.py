N = int(input())
    
if N % 4 == 0:
    print(-N)
elif (N + 1) % 4 == 0:
    print(0)
elif (N + 2) % 4 == 0:
    print(N + 1)
else:
    print(1)