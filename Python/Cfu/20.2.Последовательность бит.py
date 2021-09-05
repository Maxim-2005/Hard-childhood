arr = input()
N, P, B = map(int, input().split())

for i in range(P-1, P+N*B-1, B):
    print(int(arr[i:i+B], 2)) 