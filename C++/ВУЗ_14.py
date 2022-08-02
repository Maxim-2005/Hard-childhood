t = 0;
n = int(input());

for i in range(n):
	if (2** i >= n):
		break;
	else:
		t += 1;
	
print(t);
