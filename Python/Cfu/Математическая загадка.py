x = int(input())
c = 0
kur = []
if x >= 11 or x <= 0:
	print(-1)
else:
	while c < x:
		m = input()
		kur.append(m)
		c += 1
	for i in kur:
		k = int(i)
		if k <= 100 or (k - 100) % 7 != 0:
			print(-1)
		else:
			k = (k-100)//7
			print(k)