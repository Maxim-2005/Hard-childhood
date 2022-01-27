	x = 5
repeat
	x = x - 1
	print('repeat', x)
until(x < 0)

while x < 5 do
	x = x + 1
	print('while', x)
end

for i = 1, 5, 2 do
	print('for', i)
end

--iterator
arr = {5, 10, 15, 25, 35}
for key, i in ipairs(arr) do
	print(key, i)
end

for i = 1, #arr do
	print(arr[i])
end

--zapysk falila dofile('folder\main.lua')
--local module = require('main')

x = io.read('*n')