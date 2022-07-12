a, b = map(int, input().split());
t = a;

for i in range(b-1):
    t *= a;

print(t);
input();
