N = int(input())

for i in range(N):
	p = input()
	x = y = 0
	arr = [[x, y]]
	c = "kiborg"
	for j in range(0, len(p), 2):
	
		if p[j:j+2] == "00":
			y += 1
		elif p[j:j+2] == "01":
			x += 1
		elif p[j:j+2] == "10":
			x -= 1
		elif p[j:j+2] == "11":
			y -= 1


		if [x, y] not in arr:
			arr.append([x, y])
		else:
			c = "robot"
		
	print(len(arr), c)
	
